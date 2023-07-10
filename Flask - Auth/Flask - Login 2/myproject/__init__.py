import os
from flask import Flask, render_template, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


login_manager = LoginManager(app)
login_manager.login_view = "login"




