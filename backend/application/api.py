from datetime import datetime as dt
from flask_restful import Resource, request

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
                    "creator_name": genre.user_info.username,
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
        return "The request doesn't exist", 404


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
                if song_obj.cover_image:
                    return_json["cover_image"] = song_obj.cover_image
                else:
                    return_json["id"] = song_obj.id
                    return_json["song_name"] = song_obj.song_name
                    return_json["cover_image"] = song_obj.song_album_info.cover_image
                    return_json["album_name"] = song_obj.song_album_info.album_name
                    return_json["song_url"] = song_obj.song_url
                    return_json["lyrics_url"] = song_obj.lyrics_url
                    return_json["genre"] = song_obj.genre
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
                        return_json["Song_in_no_of_playlists"] = Playlists.query.filter(
                            PlaylistSongs.song_id == song_id
                        ).count()
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
    def post(self, id):
        """Converts a melophile or patron into creator."""
        user_obj = Users.query.filter_by(id=id).first()
        if user_obj:
            user_obj.roles.append("creator")
            db.session.commit()
            return "Time to shine on Spotlight with your creations", 200
        else:
            raise NotFound(status_code=404, error_message="User not found")


class Creator_Album_API(Resource):
    @roles_required("creator")
    @auth_required("token")
    def post(self):
        """Creates an album."""
        form_data = request.form()
        album_obj = Albums()
        album_obj.creator_id = current_user.id
        album_obj.artists_names = form_data.get("artists_names")
        album_obj.album_name = form_data.get("album_name")
        cover_image_file = form_data.files.get("cover_image")
        cover_image_file_filename = cover_image_file.filename + dt.now().strftime(
            "%Y_%m_%d_%H_%M_%S"
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
        form_data = request.form()
        album_obj = Albums.query.filter_by(id=id).first()
        if album_obj:
            if album_obj.creator_id == current_user.id:
                album_obj.artists_names = form_data.get("artists_names")
                album_obj.album_name = form_data.get("album_name")
                cover_image_file = form_data.files.get("cover_image")
                if (
                    cover_image_file
                    and album_obj.cover_image != cover_image_file.filename
                ):
                    cover_image_file_filename = (
                        cover_image_file.filename
                        + dt.now().strftime("%Y_%m_%d_%H_%M_%S")
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
        form_data = request.form()
        song_obj = Songs()
        song_obj.album_id = form_data.get("album_id")
        song_obj.name = form_data.get("name")
        song_obj_cover_image_file = form_data.files.get("cover_image")
        song_obj_audio_file = form_data.files.get("audio_file")
        song_obj_lyrics_file = form_data.files.get("lyrics_file")
        song_obj_cover_image_file_filename = (
            song_obj_cover_image_file.filename + dt.now().strftime("%Y_%m_%d_%H_%M_%S")
        )
        song_obj_audio_file_filename = song_obj_audio_file.filename + dt.now().strftime(
            "%Y_%m_%d_%H_%M_%S"
        )
        song_obj_lyrics_file_filename = (
            song_obj_lyrics_file.filename + dt.now().strftime("%Y_%m_%d_%H_%M_%S")
        )
        try:
            song_obj_cover_image_file.save(
                os.path.join(
                    pwd, "../static", "Song_Images", song_obj_cover_image_file_filename
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
        form_data = request.form()
        song_obj = Songs.query.filter_by(id=id).first()
        if song_obj:
            if song_obj.song_album_info.creator_id == current_user.id:
                song_obj.name = form_data.get("name")
                song_obj_cover_image_file = form_data.files.get("cover_image")
                song_obj_audio_file = form_data.files.get("audio_file")
                song_obj_lyrics_file = form_data.files.get("lyrics_file")
                if (
                    song_obj_cover_image_file
                    and song_obj.cover_image != song_obj_cover_image_file.filename
                ):
                    try:
                        song_obj_cover_image_file_filename = (
                            song_obj_cover_image_file.filename
                            + dt.now().strftime("%Y_%m_%d_%H_%M_%S")
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
                            song_obj_audio_file.filename
                            + dt.now().strftime("%Y_%m_%d_%H_%M_%S")
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
                            song_obj_lyrics_file.filename
                            + dt.now().strftime("%Y_%m_%d_%H_%M_%S")
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

