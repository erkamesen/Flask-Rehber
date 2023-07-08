# __init__.py 
import os 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir+"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "thisisasecretkey"

db = SQLAlchemy(app)
Migrate(app, db)

from myproject.owners.views import owner
from myproject.dogs.views import dog

app.register_blueprint(dog)
app.register_blueprint(owner)

@app.route("/")
def index():
    return render_template("home.html")


