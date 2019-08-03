# coding=utf-8
# Tuodaan Flask
from flask import Flask
app = Flask(__name__)

from functools import wraps

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reseptit.db"    
    app.config["SQLALCHEMY_ECHO"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# kirjautuminen
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi reseptikirjaa."


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            unauthorized  = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Luetaan kansiosta application tiedoston views sisältö
from application import views

from application.reseptit import models
from application.reseptit import views

from application.auth import models
from application.auth import views

from sqlalchemy import event
from sqlalchemy.engine import Engine
from application.auth.models import Role, User

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

@event.listens_for(Role.__table__, 'after_create')
def insert_initial_roles(*args, **kwargs):
    db.session.add(Role("ADMIN", True))
    db.session.add(Role("USER", False))
    db.session.commit()

@event.listens_for(User.__table__, 'after_create')
def insert_initial_superuser(*args, **kwargs):
    if os.environ.get("HEROKU"):
        super_user = User(
            os.environ.get("SU_NAME"),
            os.environ.get("SU_USERNAME"),
            os.environ.get("SU_PASSWD"),
            os.environ.get("SU_EMAIL"))
    else:
        super_user = User(
            "ADMIN",
            "admin",
            "admin",
            "admin@admin.com")
    db.session.add(super_user)
    db.session.commit()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
try: 
    db.create_all()

    # Set roles for default user with id = 1,
    # including ADMIN-role.gur
    su_user = User.query.get(1)
    su_user.set_default_role()
    su_role = Role.query.filter_by(superuser=True).first()
    if su_role.name not in su_user.get_roles():
        su_user.roles.append(su_role)
        db.session.commit()


except:
    pass
