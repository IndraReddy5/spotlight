import os
from flask import Flask
from application.config import LocalDevelopmentConfig
from application.database import db
from application.api import *
from flask_restful import Api
from flask_security import Security
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))
db = db
api = Api()


def create_app():
    app = Flask(__name__)
    if os.getenv("ENV", "development") == "production":
        raise Exception("currently no production config is setup.")
    else:
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    # Adding Api Resources
    api.add_resource(Admin_Change_Password_API, "/api/changepassword/admin")
    api.add_resource(Admin_Genre_API, "/api/admin/genre")
    api.add_resource(Admin_Flags_API, "/api/admin/flags")
    api.add_resource(Get_Stats, "/api/stats")
    api.add_resource(Remove_Song_API, "/api/remove/song/<int:id>")
    api.add_resource(Remove_Album_API, "/api/remove/album/<int:id>")
    api.add_resource(Creator_Account_Origin_API, "/api/creator/signup/<string:name>")
    api.add_resource(
        Creator_Album_API, "/api/creator/album/new", "/api/creator/album/<int:id>"
    )
    api.add_resource(
        Creator_Song_API, "/api/creator/song/new", "/api/creator/song/<int:id>"
    )
    api.add_resource(Creator_Genre_Req_API, "/api/creator/genre/new")
    api.add_resource(
        Creator_Add_Song_Genre_API,
        "/api/creator/song/<int:song_id>/add/genre/<int:genre_id>",
    )
    api.add_resource(Common_Albums_By_Creator_API, "/api/creator/<string:name>/albums")
    api.add_resource(
        Common_Playlists_By_User_API,
        "/api/user/<string:name>/playlists",
        "/api/playlist/<int:playlist_id>/songs",
        "/api/playlist/new",
        "/api/playlist/<int:id>/edit",
        "/api/playlist/<int:playlist_id>/remove/<int:song_id>",
        "/api/remove/playlist/<int:playlist_id>",
    )
    api.add_resource(Common_Search_API, "/api/search/song")
    api.add_resource(Common_Get_Role_API, "/api/getrole")
    api.add_resource(Patron_Download_API, "/api/download")
    api.add_resource(Patron_Subscribe_API, "/api/patron/<string:name>/subscribe")
    api.add_resource(Melophile_User_Account_API, "/api/signup")
    api.add_resource(Melophile_Flag_Song_API, "/api/flag/song/<int:id>")
    api.add_resource(Melophile_Flag_Album_API, "/api/flag/album/<int:id>")
    api.add_resource(Melophile_Rate_Song_API, "/api/song/<int:id>/rating")
    api.add_resource(Melophile_Lyrics_API, "/api/song/<int:song_id>/lyrics")
    api.add_resource(
        Melophile_Add_Song_Playlist_API,
        "/api/playlist/<int:playlist_id>/add/<int:song_id>",
    )
    app.security = Security(app, user_datastore)
    api.init_app(app)
    CORS(app)

    return app
