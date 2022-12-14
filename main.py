from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    # Create the flask app object
    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    # this makes db_commands available
    from commands import db_commands
    app.register_blueprint(db_commands)


    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)


    return app

