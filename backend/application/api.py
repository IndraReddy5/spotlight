from datetime import timedelta, datetime as dt
from flask_restful import Resource, request
from flask import send_file
import zipfile

from application.database import db
from application.models import *
from application.errors import *

from flask_security import (
    auth_required,
    SQLAlchemyUserDatastore,
    hash_password,
    roles_required,
    current_user,
    roles_accepted,
)
from application.utils import *

import os
import json

pwd = os.path.abspath(os.path.dirname(__file__))
user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)


### JS Console Login API Fetch Request Test Code
"""
let data = {'username':'admin','password':'light123'}
fetch("http://127.0.0.1:8000/api/login?include_auth_token",
{headers:{'content-type': 'application/json'},
'method':'POST','body':JSON.stringify(data)})
.then(response => response.json())
.then(data => console.log(data))
"""


### Admin APIs
class Admin_Change_Password_API(Resource):
    @roles_required("admin")
    @auth_required("token")
    def put(self):
        """Changes Admin Password."""
        form_data = request.get_json()
        u_obj = Users.query.filter_by(username=form_data.get("username")).first()
        if u_obj:
            u_obj.password = hash_password(form_data.get("password"))
            db.session.commit()
            return "Password Changed", 200
        else:
            raise NotFound(status_code=404, error_message="User not found")


class Admin_Genre_API(Resource):
    @roles_required("admin")
    @auth_required("token")
    def get(self):
        """Fetches all pending genre creation requests."""
        req_genres = Genre.query.filter_by(active="pending").all()
        if req_genres:
            return_json = {}
            for genre in req_genres:
                return_json[genre.id] = {
                    "genre": genre.genre,
                    "creator_id": genre.requested_by,
                    "creator_name": Users.query.filter_by(id=genre.requested_by)
                    .first()
                    .username,
                }
            return json.dumps(return_json), 200
        else:
            return "No pending genre creation requests", 200

    @roles_required("admin")
    @auth_required("token")
    def post(self):
        """Accepts or Rejects a genre request."""
        ### Enhancement to do, send a mail to the creator through a cron job describing what admin has decided
        form_data = request.get_json()
        genre = Genre.query.filter_by(id=form_data.get("genre_id")).first()
        if genre:
            genre.admin_approval = form_data.get("admin_approval")
            db.session.commit()
            return "Genre request updated", 200
        raise NotFound(status_code=404, error_message="Genre not found")


class Admin_Flags_API(Resource):
    @roles_required("admin")
    @auth_required("token")
    def get(self):
        """Fetches all pending flags for songs and albums."""
        return_json = {"songs": [], "albums": []}
        song_flags = SongsFlagged.query.filter_by(admin_read=False).all()
        album_flags = AlbumsFlagged.query.filter_by(admin_read=False).all()
        if song_flags:
            for flag in song_flags:
                return_json["songs"][flag.id] = {
                    "song_id": flag.song_id,
                    "flagged_by": flag.melophile_id,
                    "flagged_by_name": flag.user_info.username,
                    "reason": flag.reason,
                    "flagged_on": prettify_date(flag.date_time),
                }
        if album_flags:
            for flag in album_flags:
                return_json["albums"][flag.id] = {
                    "album_id": flag.album_id,
                    "flagged_by": flag.melophile_id,
                    "flagged_by_name": flag.user_info.username,
                    "reason": flag.reason,
                    "flagged_on": prettify_date(flag.date_time),
                }
        if song_flags or album_flags:
            return json.dumps(return_json), 200
        else:
            return "No pending flags", 200

    @roles_required("admin")
    @auth_required("token")
    def post(self):
        """Marks the flag as read by the admin."""
        form_data = request.get_json()
        flag_type = form_data.get("flag_type")
        flag_id = form_data.get("flag_id")
        if flag_type == "song":
            flag_item = SongsFlagged.query.filter_by(id=flag_id).first()
            flag_item.admin_read = True
            db.session.commit()
            return "Flag marked as read", 200
        elif flag_type == "album":
            flag_item = AlbumsFlagged.query.filter_by(id=flag_id).first()
            flag_item.admin_read = True
            db.session.commit()
            return "Flag marked as read", 200
        else:
            return "Invalid Request", 400


class Get_Stats(Resource):
    @auth_required("token")
    def get(self):
        """Get stats of a song or album."""
        album_id = request.args.get("album_id")
        song_id = request.args.get("song_id")
        return_json = {}
        if song_id:
            song_obj = Songs.query.filter_by(id=song_id).first()
            if song_obj:
                return_json["id"] = song_obj.id
                return_json["song_name"] = song_obj.name
                if song_obj.cover_image:
                    return_json["cover_image"] = (
                        "static/Song_Images/" + song_obj.cover_image
                    )
                else:
                    return_json["cover_image"] = (
                        "static/Album_Images/" + song_obj.song_album_info.cover_image
                    )
                return_json["album_name"] = song_obj.song_album_info.album_name
                return_json["song_url"] = "static/songs/" + song_obj.song_url
                return_json["lyrics_url"] = "static/lyrics/" + song_obj.lyrics_url
                return_json["genre"] = [
                    x.genre_table.genre
                    for x in SongGenre.query.filter_by(song_id=song_id).all()
                ]
                return_json["duration"] = song_obj.duration
                return_json["release_date"] = prettify_date(song_obj.release_date)
                return_json["artists"] = song_obj.song_album_info.artists_names
                return_json["rating"] = rating_avg(
                    SongRatings.query.with_entities(SongRatings.rating)
                    .filter_by(song_id=song_id)
                    .all()
                )
                if "admin" in current_user.roles:
                    return_json["flags_on_song"] = SongsFlagged.query.filter_by(
                        song_id=song_id
                    ).count()
                    return_json[
                        "Song_in_no_of_playlists"
                    ] = PlaylistSongs.query.filter_by(song_id=song_id).count()
                return json.dumps(return_json), 200
            else:
                raise NotFound(status_code=404, error_message="Song not found")
        else:
            album_obj = Albums.query.filter_by(id=album_id).first()
            if album_obj:
                return_json["artists"] = album_obj.artists_names
                return_json["album_name"] = album_obj.album_name
                return_json["cover_image"] = album_obj.cover_image
                return_json["total_no_songs"] = album_obj.album_songs.count()
                # Todo return songs_info along with album info
                if "admin" in current_user.roles:
                    return_json["flags_on_album"] = AlbumsFlagged.query.filter_by(
                        album_id=album_id
                    ).count()
                return json.dumps(return_json), 200
            else:
                raise NotFound(status_code=404, error_message="Album not found")


class Remove_Song_API(Resource):
    @roles_accepted("admin", "creator")
    @auth_required("token")
    def delete(self, id):
        """Removes a song from the database."""
        song_obj = Songs.query.filter_by(id=id).first()
        if song_obj:
            if (song_obj.song_album_info.creator_id == current_user.id) or (
                "admin" in current_user.roles
            ):
                playlist_obj_to_be_deleted = PlaylistSongs.query.filter_by(
                    song_id=id
                ).all()
                for song in playlist_obj_to_be_deleted:
                    db.session.delete(song)
                rating_objs_to_be_deleted = SongRatings.query.filter_by(
                    song_id=id
                ).all()
                for rating in rating_objs_to_be_deleted:
                    db.session.delete(rating)
                # Deleting files of song, cover_image and its lyrics from the storage
                if song_obj.song_url:
                    os.remove(
                        os.path.join(pwd, "../static", "songs", song_obj.song_url)
                    )
                if song_obj.cover_image:
                    os.remove(
                        os.path.join(
                            pwd, "../static", "Song_Images", song_obj.cover_image
                        )
                    )
                if song_obj.lyrics_url:
                    os.remove(
                        os.path.join(pwd, "../static", "lyrics", song_obj.lyrics_url)
                    )
                db.session.delete(song_obj)
                db.session.commit()

                ### Todo - Enhancement
                # Trigger a cron job, sending a notification to creator and users who have added the song to their playlists
                return "Song removed", 200
            else:
                raise Unauthorized(error_message="you cannot delete this song")
        else:
            raise NotFound(status_code=404, error_message="Song not found")


class Remove_Album_API(Resource):
    @roles_accepted("admin", "creator")
    @auth_required("token")
    def delete(self, id):
        """Removes an album from the database."""
        album_obj = Albums.query.filter_by(id=id).first()
        if album_obj:
            if (album_obj.creator_id == current_user.id) or (
                "admin" in current_user.roles
            ):
                songs_objs_to_be_deleted = Songs.query.filter_by(album_id=id).all()
                for song in songs_objs_to_be_deleted:
                    playlist_objs_to_be_deleted = Playlists.query.filter_by(
                        song_id=song.id
                    ).all()
                    for playlist_obj in playlist_objs_to_be_deleted:
                        db.session.delete(playlist_obj)
                    ratings_objs_to_be_deleted = SongRatings.query.filter_by(
                        song_id=song.id
                    ).all()
                    for rating in ratings_objs_to_be_deleted:
                        db.session.delete(rating)
                    # Deleting files of song, cover_image and its lyrics from the storage
                    if song.song_url:
                        os.remove(
                            os.path.join(pwd, "../static", "songs", song.song_url)
                        )
                    if song.cover_image:
                        os.remove(
                            os.path.join(
                                pwd, "../static", "Song_Images", song.cover_image
                            )
                        )
                    if song.lyrics_url:
                        os.remove(
                            os.path.join(pwd, "../static", "lyrics", song.lyrics_url)
                        )
                    db.session.delete(song)
                if album_obj.cover_image:
                    os.remove(
                        os.path.join(
                            pwd, "../static", "Album_Images", album_obj.cover_image
                        )
                    )
                db.session.delete(album_obj)
                db.session.commit()

                ### Todo - Enhancement
                # Trigger a cron job, sending a notification to creator and users who have added the album songs to their playlists
                return "Album removed", 200
            else:
                raise Unauthorized(error_message="you cannot delete this album")
        else:
            raise NotFound(status_code=404, error_message="Album not found")


### Creator APIs


class Creator_Account_Origin_API(Resource):
    @roles_accepted("patron", "melophile", "admin")
    @auth_required("token")
    def post(self, name):
        """Converts a melophile or patron into creator."""
        user_obj = Users.query.filter_by(username=name).first()
        if user_obj:
            user_datastore.add_role_to_user(user_obj, "creator")
            db.session.commit()
            return "Time to shine on Spotlight with your creations", 200
        else:
            raise NotFound(status_code=404, error_message="User not found")


class Creator_Album_API(Resource):
    @roles_required("creator")
    @auth_required("token")
    def post(self):
        """Creates an album."""
        form_data = request.form
        album_obj = Albums()
        album_obj.creator_id = current_user.id
        album_obj.artists_names = form_data.get("artists_names")
        album_obj.album_name = form_data.get("album_name")
        cover_image_file = request.files["cover_image"]
        cover_image_file_filename = (
            dt.now().strftime("%Y_%m_%d_%H_%M_%S") + cover_image_file.filename
        )
        try:
            cover_image_file.save(
                os.path.join(
                    pwd, "../static", "Album_Images", cover_image_file_filename
                )
            )
            album_obj.cover_image = cover_image_file_filename
        except:
            raise InternalServerError(
                status_code=500,
                error_code="sav_file_e",
                error_message="Error saving cover image file",
            )
        db.session.add(album_obj)
        db.session.commit()
        return "Album created", 200

    @roles_required("creator")
    @auth_required("token")
    def put(self, id):
        """Edits Album Details."""
        form_data = request.form
        album_obj = Albums.query.filter_by(id=id).first()
        if album_obj:
            if album_obj.creator_id == current_user.id:
                album_obj.artists_names = form_data.get("artists_names")
                album_obj.album_name = form_data.get("album_name")
                cover_image_file = request.files.get("cover_image")
                if (
                    cover_image_file
                    and album_obj.cover_image != cover_image_file.filename
                ):
                    cover_image_file_filename = (
                        dt.now().strftime("%Y_%m_%d_%H_%M_%S")
                        + cover_image_file.filename
                    )
                    try:
                        cover_image_file.save(
                            os.path.join(
                                pwd,
                                "../static",
                                "Album_Images",
                                cover_image_file_filename,
                            )
                        )
                        os.remove(
                            os.path.join(
                                pwd, "../static", "Album_Images", album_obj.cover_image
                            )
                        )
                        album_obj.cover_image = cover_image_file_filename
                    except:
                        raise InternalServerError(
                            status_code=500,
                            error_code="sav_file_e",
                            error_message="Error saving cover image file",
                        )
                db.session.commit()
                return "Album edited", 200
            else:
                raise Unauthorized(error_message="you cannot edit this album")
        else:
            raise NotFound(status_code=404, error_message="Album not found")


class Creator_Song_API(Resource):
    @roles_required("creator")
    @auth_required("token")
    def post(self):
        """Creates a song."""
        form_data = request.form
        song_obj = Songs()
        song_obj.album_id = form_data.get("album_id")
        song_obj.name = form_data.get("song_name")
        song_obj_cover_image_file = None
        if len(request.files) == 3:
            song_obj_cover_image_file = request.files["cover_image"]
        song_obj_audio_file = request.files["audio_file"]
        song_obj_lyrics_file = request.files["lyrics_file"]
        if song_obj_cover_image_file:
            song_obj_cover_image_file_filename = (
                dt.now().strftime("%Y_%m_%d_%H_%M_%S")
                + song_obj_cover_image_file.filename
            )
        song_obj_audio_file_filename = (
            dt.now().strftime("%Y_%m_%d_%H_%M_%S") + song_obj_audio_file.filename
        )
        song_obj_lyrics_file_filename = (
            dt.now().strftime("%Y_%m_%d_%H_%M_%S")
        ) + song_obj_lyrics_file.filename
        try:
            if song_obj_cover_image_file:
                song_obj_cover_image_file.save(
                    os.path.join(
                        pwd,
                        "../static",
                        "Song_Images",
                        song_obj_cover_image_file_filename,
                    )
                )
                song_obj.cover_image = song_obj_cover_image_file_filename
            song_obj_audio_file.save(
                os.path.join(pwd, "../static", "songs", song_obj_audio_file_filename)
            )
            song_obj.song_url = song_obj_audio_file_filename
            song_obj_lyrics_file.save(
                os.path.join(pwd, "../static", "lyrics", song_obj_lyrics_file_filename)
            )
            song_obj.lyrics_url = song_obj_lyrics_file_filename
            song_obj.release_date = dt.now()
            song_obj.duration = form_data.get("duration")
        except:
            raise InternalServerError(
                status_code=500,
                error_code="sav_file_e",
                error_message="Error saving files",
            )
        db.session.add(song_obj)
        db.session.commit()
        return "Song created", 200

    @roles_required("creator")
    @auth_required("token")
    def put(self, id):
        """Edits song details."""
        form_data = request.form
        song_obj = Songs.query.filter_by(id=id).first()
        if song_obj:
            if song_obj.song_album_info.creator_id == current_user.id:
                song_obj.name = form_data.get("name")
                song_obj_cover_image_file = request.files["cover_image"]
                song_obj_audio_file = request.files["audio_file"]
                song_obj_lyrics_file = request.files["lyrics_file"]
                if (
                    song_obj_cover_image_file
                    and song_obj.cover_image != song_obj_cover_image_file.filename
                ):
                    try:
                        song_obj_cover_image_file_filename = (
                            dt.now().strftime("%Y_%m_%d_%H_%M_%S")
                            + song_obj_cover_image_file.filename
                        )
                        song_obj_cover_image_file.save(
                            os.path.join(
                                pwd,
                                "../static",
                                "Song_Images",
                                song_obj_cover_image_file_filename,
                            )
                        )
                        os.remove(
                            os.path.join(
                                pwd, "../static", "Song_Images", song_obj.cover_image
                            )
                        )

                        song_obj.cover_image = song_obj_cover_image_file_filename
                    except:
                        raise InternalServerError(
                            status_code=500,
                            error_code="sav_file_e",
                            error_message="Error saving files",
                        )
                if (
                    song_obj_audio_file
                    and song_obj.song_url != song_obj_audio_file.filename
                ):
                    try:
                        song_obj_audio_file_filename = (
                            dt.now().strftime("%Y_%m_%d_%H_%M_%S")
                            + song_obj_audio_file.filename
                        )
                        song_obj_audio_file.save(
                            os.path.join(
                                pwd, "../static", "songs", song_obj_audio_file_filename
                            )
                        )
                        os.remove(
                            os.path.join(pwd, "../static", "songs", song_obj.song_url)
                        )
                        song_obj.song_url = song_obj_audio_file_filename

                    except:
                        raise InternalServerError(
                            status_code=500,
                            error_code="sav_file_e",
                            error_message="Error saving files",
                        )
                if (
                    song_obj_lyrics_file
                    and song_obj.lyrics_url != song_obj_lyrics_file.filename
                ):
                    try:
                        song_obj_lyrics_file_filename = (
                            dt.now().strftime("%Y_%m_%d_%H_%M_%S")
                            + song_obj_lyrics_file.filename
                        )
                        song_obj_lyrics_file.save(
                            os.path.join(
                                pwd,
                                "../static",
                                "lyrics",
                                song_obj_lyrics_file_filename,
                            )
                        )
                        os.remove(
                            os.path.join(
                                pwd, "../static", "lyrics", song_obj.lyrics_url
                            )
                        )

                        song_obj.lyrics_url = song_obj_lyrics_file_filename
                    except:
                        raise InternalServerError(
                            status_code=500,
                            error_code="sav_file_e",
                            error_message="Error saving files",
                        )

            else:
                raise Unauthorized(error_message="you cannot edit this song")

        else:
            raise NotFound(status_code=404, error_message="Song not found")


class Creator_Genre_Req_API(Resource):
    @roles_required("creator")
    @auth_required("token")
    def post(self):
        """Creates a genre request."""
        form_data = request.get_json()
        genre_obj = Genre()
        genre_obj.genre = form_data.get("genre")
        genre_obj.requested_by = current_user.id
        db.session.add(genre_obj)
        db.session.commit()
        return "Genre request created", 200


class Creator_Add_Song_Genre_API(Resource):
    @roles_accepted("creator", "admin")
    @auth_required("token")
    def post(self, song_id, genre_id):
        """Adds song to a genre."""
        song_genre_obj = SongGenre()
        song_obj = Songs.query.filter_by(id=song_id).first()
        genre_obj = Genre.query.filter_by(id=genre_id).first()
        song_genre_obj = SongGenre.query.filter_by(
            song_id=song_id, genre_id=genre_id
        ).first()
        if not song_genre_obj:
            if song_obj and genre_obj:
                print(
                    song_obj.song_album_info.creator_id,
                    current_user.id,
                    current_user.has_role("admin"),
                )
                if genre_obj.admin_approval == "Yes":
                    if (
                        song_obj.song_album_info.creator_id == current_user.id
                        or current_user.has_role("admin")
                    ):
                        song_genre_obj.song_id = song_id
                        song_genre_obj.genre_id = genre_id
                        db.session.add(song_genre_obj)
                        db.session.commit()
                    else:
                        raise Unauthorized(
                            error_message="you cannot add this song to genre"
                        )
                else:
                    raise Unauthorized(
                        error_message=f"The {genre_obj.genre} is not approved by admin"
                    )
            else:
                raise NotFound(status_code=404, error_message="Song or Genre not found")
        return "Song added to genre", 200


### Common APIs


class Common_Song_Play_API(Resource):
    @auth_required("token")
    def get(self, id):
        # Todo
        return "Song played", 200


class Common_Albums_By_Creator_API(Resource):
    @auth_required("token")
    def get(self):
        """Fetches all albums of a creator."""
        creator_name = request.args.get("creator_name")
        if creator_name:
            user = Users.query.filter_by(username=creator_name).first()
            albums = Albums.query.filter_by(creator_id=user.id).all()
        else:
            albums = Albums.query.all()
        if albums:
            return_json = {}
            for album in albums:
                return_json[album.id] = {
                    "album_name": album.album_name,
                    "cover_image": album.cover_image,
                    "artists": album.artists_names,
                    "no_of_songs": album.album_songs.count(),
                }
            return json.dumps(return_json), 200
        else:
            return "No albums found", 200


class Common_Playlists_Lists_By_User_API(Resource):
    @auth_required("token")
    def get(self, name):
        """Fetches all playlists of a user."""
        user = Users.query.filter_by(username=name).first()
        playlists = Playlists.query.filter_by(melophile_id=user.id).all()
        if playlists:
            return_json = {}
            for playlist in playlists:
                return_json[playlist.id] = {
                    "playlist_name": playlist.name,
                    "no_of_songs": len(playlist.playlist_songs),
                }
            return json.dumps(return_json), 200
        else:
            return "No playlists found", 200


class Common_Playlists_By_User_API(Resource):
    @auth_required("token")
    def get(self, playlist_id):
        """Fetches all songs of a playlist."""
        playlist_obj = Playlists.query.filter_by(id=playlist_id).first()
        if playlist_obj:
            if playlist_obj.user_id == current_user.id:
                return_json = {}
                for song in playlist_obj.playlist_songs:
                    return_json[song.id] = {
                        "song_id": song.song_id,
                        "song_name": song.song_info.name,
                        "cover_image": song.song_info.cover_image,
                        "album_name": song.song_info.song_album_info.album_name,
                        "artists": song.song_info.song_album_info.artists_names,
                    }
                return json.dumps(return_json), 200
            else:
                raise Unauthorized(error_message="you cannot view this playlist")
        else:
            raise NotFound(status_code=404, error_message="Playlist not found")

    @auth_required("token")
    def post(self):
        """Creates a playlist."""
        form_data = request.get_json()
        playlist_obj = Playlists()
        playlist_obj.melophile_id = current_user.id
        playlist_obj.name = form_data.get("playlist_name")
        db.session.add(playlist_obj)
        db.session.commit()
        return "Playlist created", 200

    @auth_required("token")
    def put(self, id):
        """Edits a playlist."""
        form_data = request.get_json()
        playlist_obj = Playlists.query.filter_by(id=id).first()
        if playlist_obj:
            if playlist_obj.user_id == current_user.id:
                playlist_obj.playlist_name = form_data.get("playlist_name")
                db.session.commit()
                return "Playlist edited", 200
            else:
                raise Unauthorized(error_message="you cannot edit this playlist")
        else:
            raise NotFound(status_code=404, error_message="Playlist not found")

    @auth_required("token")
    def delete(self, playlist_id, song_id):
        """Removes a song from a playlist."""
        playlist_obj = Playlists.query.filter_by(id=playlist_id).first()
        if playlist_obj:
            if playlist_obj.user_id == current_user.id:
                playlist_song_obj = PlaylistSongs.query.filter_by(
                    playlist_id=playlist_id, song_id=song_id
                ).first()
                if playlist_song_obj:
                    db.session.delete(playlist_song_obj)
                    db.session.commit()
                    return "Song removed from playlist", 200
                else:
                    raise NotFound(
                        status_code=404, error_message="Song not found in playlist"
                    )
            else:
                raise Unauthorized(error_message="you cannot delete this playlist")
        else:
            raise NotFound(status_code=404, error_message="Playlist not found")

    @auth_required("token")
    def delete(self, playlist_id):
        """Deletes a playlist."""
        playlist_obj = Playlists.query.filter_by(id=playlist_id).first()
        if playlist_obj:
            if playlist_obj.user_id == current_user.id:
                playlist_songs_objs_to_be_deleted = PlaylistSongs.query.filter_by(
                    playlist_id=playlist_id
                ).all()
                for playlist_song in playlist_songs_objs_to_be_deleted:
                    db.session.delete(playlist_song)
                db.session.delete(playlist_obj)
                db.session.commit()
                return "Playlist deleted", 200
            else:
                raise Unauthorized(error_message="you cannot delete this playlist")
        else:
            raise NotFound(status_code=404, error_message="Playlist not found")


class Common_Search_API(Resource):
    @auth_required("token")
    def get(self):
        """Returns url for the song file."""
        song_id = request.args.get("song_id")
        song_obj = Songs.query.filter_by(id=song_id).first()
        if song_obj:
            return (
                os.path.join(
                    os.getenv("BACKEND_URL"), "../static", "songs", song_obj.song_url
                ),
                200,
            )
        else:
            raise NotFound(status_code=404, error_message="Song not found")


class Common_Creator_Avg_Rating_API(Resource):
    @auth_required("token")
    def get(self, name):
        """Returns avg rating for all songs of the creator."""
        usr_obj = Users.query.filter_by(username=name).first()
        if usr_obj:
            albums_objs = Albums.query.filter_by(creator_id=usr_obj.id).all()
            if albums_objs:
                avg_ratings = []
                for album in albums_objs:
                    for song in album.album_songs:
                        avg_ratings.append(
                            rating_avg(
                                SongRatings.query.with_entities(SongRatings.rating)
                                .filter_by(song_id=song.id)
                                .all()
                            )
                        )
                if avg_ratings:
                    return sum(avg_ratings) / len(avg_ratings), 200
            return 0, 200
        else:
            raise NotFound(status_code=404, error_message="User not found")


class Common_Get_Role_API(Resource):
    @auth_required("token")
    def post(self):
        """Returns role of a user."""
        priority_roles = ["admin", "creator", "patron", "melophile"]
        for role in priority_roles:
            if current_user.has_role(role):
                return role, 200


class Common_Get_Songs_List_API(Resource):
    @auth_required("token")
    def get(self):
        """Returns all songs sorted by rating or release date."""
        sort_by = request.args.get("sort_by")
        limit = request.args.get("limit")
        songs = Songs.query.all()
        return_json = {}
        for song_obj in songs:
            return_json[song_obj.id] = {}
            return_json[song_obj.id]["song_name"] = song_obj.name
            if song_obj.cover_image:
                return_json[song_obj.id]["cover_image"] = (
                    "static/Song_Images/" + song_obj.cover_image
                )
            else:
                return_json[song_obj.id]["cover_image"] = (
                    "static/Album_Images/" + song_obj.song_album_info.cover_image
                )
            return_json[song_obj.id]["album_name"] = song_obj.song_album_info.album_name
            return_json[song_obj.id]["song_url"] = "static/songs/" + song_obj.song_url
            return_json[song_obj.id]["lyrics_url"] = (
                "static/lyrics/" + song_obj.lyrics_url
            )
            return_json[song_obj.id]["genre"] = [
                x.genre_table.genre
                for x in SongGenre.query.filter_by(song_id=song_obj.id).all()
            ]
            return_json[song_obj.id]["duration"] = song_obj.duration
            return_json[song_obj.id]["release_date"] = song_obj.release_date
            return_json[song_obj.id]["artists"] = song_obj.song_album_info.artists_names
            return_json[song_obj.id]["rating"] = rating_avg(
                SongRatings.query.with_entities(SongRatings.rating)
                .filter_by(song_id=song_obj.id)
                .all()
            )
        if sort_by == "rating":
            return_json = sort_by_rating(return_json)
        elif sort_by == "release_date":
            return_json = sort_by_date(return_json)
        else:
            pass
        for song in return_json:
            return_json[song]["release_date"] = prettify_date(
                return_json[song]["release_date"]
            )
        if limit:
            return_json = dict(list(return_json.items())[:int(limit)])
        return return_json, 200


### Patron APIs


class Patron_Download_API(Resource):
    @roles_accepted("patron", "creator")
    @auth_required("token")
    def get(self):
        """Downloads a song or songs in an album."""
        song_id = request.args.get("song_id")
        album_id = request.args.get("album_id")
        if song_id:
            song_obj = Songs.query.filter_by(id=song_id).first()
            if song_obj:
                if song_obj.song_url:
                    return send_file(
                        os.path.join(pwd, "../static", "songs", song_obj.song_url),
                        as_attachment=True,
                    )
                else:
                    raise NotFound(status_code=404, error_message="Song not found")
            else:
                raise NotFound(status_code=404, error_message="Song not found")
        elif album_id:
            album_obj = Albums.query.filter_by(id=album_id).first()
            if album_obj:
                zip_file = zipfile.ZipFile(
                    os.path.join(
                        pwd, "../static", "Albums", album_obj.album_name + ".zip"
                    ),
                    "w",
                )
                for song in album_obj.album_songs:
                    if song.song_url:
                        zip_file.write(
                            os.path.join(pwd, "../static", "songs", song.song_url)
                        )
                    else:
                        raise NotFound(status_code=404, error_message="Song not found")
                zip_file.close()
                return send_file(
                    os.path.join(
                        pwd, "../static", "Albums", album_obj.album_name + ".zip"
                    ),
                    as_attachment=True,
                )
            else:
                raise NotFound(status_code=404, error_message="Album not found")
        else:
            raise BadRequest(
                error_message="Missing arguments, please include song_id or album_id"
            )


class Patron_Subscribe_API(Resource):
    @roles_accepted("melophile", "admin")
    @auth_required("token")
    def post(self, name):
        """Converts a melophile into patron."""
        user_obj = Users.query.filter_by(username=name).first()
        if user_obj:
            user_datastore.add_role_to_user(user_obj, "patron")
            user_sub_obj = UserSubscriptions()
            user_sub_obj.melophile_id = current_user.id
            user_sub_obj.subscription_ending = dt.now() + timedelta(days=365)
            db.session.add(user_sub_obj)
            db.session.commit()
            return "You are now a patron", 200
        else:
            raise NotFound(status_code=404, error_message="User not found")


### Melophile APIs


class Melophile_User_Account_API(Resource):
    def post(self):
        """Creates a Melophile account on Spotlight."""
        form_data = request.get_json()
        username = form_data.get("username")
        email = form_data.get("email")
        password = hash_password(form_data.get("password"))
        melophile_role = user_datastore.find_role("melophile")
        if user_datastore.find_user(username=username):
            raise ValidationError(
                status_code=400,
                error_code="usr_1",
                error_message="A user exists with same username, please pick other username",
            )
        elif user_datastore.find_user(email=email):
            raise ValidationError(
                status_code=400,
                error_code="usr_2",
                error_message="You have account with same email, if you forgot account details contact support@spotlight.in",
            )
        else:
            user_datastore.create_user(
                username=username,
                email=email,
                password=password,
                roles=[melophile_role],
            )
            db.session.commit()
        return "Melophile account created", 200


class Melophile_Flag_Song_API(Resource):
    @auth_required("token")
    def post(self, id):
        """Flags a song"""
        form_data = request.get_json()
        reason = form_data.get("reason")
        song_obj = Songs.query.filter_by(id=id).first()
        if song_obj:
            song_flag_obj = SongsFlagged()
            song_flag_obj.song_id = id
            song_flag_obj.melophile_id = current_user.id
            song_flag_obj.reason = reason
            song_obj.date_time = dt.now()
            db.session.add(song_flag_obj)
            db.session.commit()
            return "Song flagged", 200
        else:
            raise NotFound(status_code=404, error_message="Song not found")


class Melophile_Flag_Album_API(Resource):
    @auth_required("token")
    def post(self, id):
        """Flags an album"""
        form_data = request.get_json()
        reason = form_data.get("reason")
        album_obj = Albums.query.filter_by(id=id).first()
        if album_obj:
            album_flag_obj = AlbumsFlagged()
            album_flag_obj.album_id = id
            album_flag_obj.melophile_id = current_user.id
            album_flag_obj.reason = reason
            album_flag_obj.date_time = dt.now()
            db.session.add(album_flag_obj)
            db.session.commit()
            return "Album flagged", 200
        else:
            raise NotFound(status_code=404, error_message="Album not found")


class Melophile_Rate_Song_API(Resource):
    @roles_accepted("melophile", "patron")
    @auth_required("token")
    def post(self, id):
        """Rates a song"""
        form_data = request.get_json()
        rating = form_data.get("rating")
        song_obj = Songs.query.filter_by(id=id).first()
        if song_obj:
            song_rating_obj = SongRatings()
            song_rating_obj.song_id = id
            song_rating_obj.melophile_id = current_user.id
            song_rating_obj.rating = rating
            db.session.add(song_rating_obj)
            db.session.commit()
            return "Thank you for giving feedback on the song", 200
        else:
            raise NotFound(status_code=404, error_message="Song not found")


class Melophile_Lyrics_API(Resource):
    @auth_required("token")
    def get(self, song_id):
        """returns a link to file containing lyrics of a song"""
        song_obj = Songs.query.filter_by(id=song_id).first()
        if song_obj:
            if song_obj.lyrics_url:
                return (
                    os.path.join(
                        os.getenv("BACKEND_URL"),
                        "../static",
                        "lyrics",
                        song_obj.lyrics_url,
                    ),
                )
            else:
                raise NotFound(status_code=404, error_message="Lyrics not found")
        else:
            raise NotFound(status_code=404, error_message="Song not found")


class Melophile_Add_Song_Playlist_API(Resource):
    @auth_required("token")
    def post(self, playlist_id, song_id):
        """Adds a song to a playlist."""
        playlist_obj = Playlists.query.filter_by(id=playlist_id).first()
        if playlist_obj:
            if playlist_obj.melophile_id == current_user.id:
                song_obj = Songs.query.filter_by(id=song_id).first()
                if song_obj:
                    playlist_song_obj = PlaylistSongs()
                    playlist_song_obj.playlist_id = playlist_id
                    playlist_song_obj.song_id = song_id
                    db.session.add(playlist_song_obj)
                    db.session.commit()
                    return "Song added to playlist", 200
                else:
                    raise NotFound(status_code=404, error_message="Song not found")
            else:
                raise Unauthorized(error_message="you cannot add to this playlist")
        else:
            raise NotFound(status_code=404, error_message="Playlist not found")
