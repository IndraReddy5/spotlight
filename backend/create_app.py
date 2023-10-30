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
    app.security = Security(app, user_datastore)
    api.init_app(app)
    CORS(app)

    return app