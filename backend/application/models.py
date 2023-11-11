from .database import db
from flask_security import UserMixin, RoleMixin


class RolesUsers(db.Model):
    __tablename__ = "roles_users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


class Roles(db.Model, RoleMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    fs_uniquifier = db.Column(db.String, unique=True, nullable=False)
    fs_token_uniquifier = db.Column(db.String, unique=True, nullable=False)
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    active = db.Column(db.String)
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    roles = db.relationship(
        "Roles",
        secondary=RolesUsers.__table__,
        backref=db.backref("users", lazy="dynamic"),
    )


class Albums(db.Model):
    __tablename__ = "albums"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    artists_names = db.Column(db.String, nullable=False)
    album_name = db.Column(db.String, nullable=False)
    cover_image = db.Column(db.String, nullable=False)
    album_songs = db.relationship(
        "Songs",
        foreign_keys="Songs.album_id",
        backref=db.backref("song_album_info"),
        lazy="dynamic",
    )


class Songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"))
    name = db.Column(db.String)
    cover_image = db.Column(db.String)
    song_url = db.Column(db.String)
    lyrics_url = db.Column(db.String)
    genre = db.Column(db.Integer)
    duration = db.Column(db.Integer)  # in seconds
    release_date = db.Column(db.DateTime)


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre = db.Column(db.String)
    admin_approval = db.Column(db.String, default="Pending")
    requested_by = db.Column(db.Integer, db.ForeignKey("users.id"))


class SongGenre(db.Model):
    __tablename__ = "song_genre"
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), primary_key=True)
    __table_args__ = (db.UniqueConstraint("song_id", "genre_id"),)


class Playlists(db.Model):
    __tablename__ = "playlists"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    melophile_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String)


class PlaylistSongs(db.Model):
    __tablename__ = "playlist_songs"
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)
    __table_args__ = (db.UniqueConstraint("playlist_id", "song_id"),)


class SongRatings(db.Model):
    __tablename__ = "song_ratings"
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)
    melophile_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    rating = db.Column(db.Integer)
    __table_args__ = (db.UniqueConstraint("song_id", "melophile_id"),)


class UserSubscriptions(db.Model):
    __tablename__ = "user_subscriptions"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    melophile_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    subscription_type = db.Column(db.String)
    admin_approval = db.Column(db.Boolean, default=False)
    subscription_ending = db.Column(db.DateTime)


class SongsFlagged:
    __tablename__ = "songs_flagged"
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))
    melophile_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reason = db.Column(db.String)
    date_time = db.Column(db.DateTime)
    admin_read = db.Column(db.Boolean, default=False)
    user_info = db.relationship("Users", foreign_keys="Users.id")
    __table_args__ = (db.UniqueConstraint("song_id", "user_id"),)


class AlbumsFlagged:
    __table_name__ = "albums_flagged"
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"))
    melophile_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reason = db.Column(db.String)
    date_time = db.Column(db.DateTime)
    admin_read = db.Column(db.Boolean, default=False)
    user_info = db.relationship("Users", foreign_keys="Users.id")
    __table_args__ = (db.UniqueConstraint("song_id", "user_id"),)
