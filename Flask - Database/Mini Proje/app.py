from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from forms import AddForm, DelForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecretkey"


############################################################################################
################################################## SQL BÖLÜMÜ ####################################################################
#############################################################################################


basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Dog(db.Model):

    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Köpeğin ismi {self.name}"


############################################################################################
################################# VIEW FONKSIYONLARI - FORMLAR #############################
#############################################################################################


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_dog = Dog(name)
        db.session.add(new_dog)
        db.session.commit()

        return redirect(url_for("list_dog"))
    return render_template("add.html", form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        dog = Dog.query.get(id)
        db.session.delete(dog)
        db.session.commit()
        return redirect(url_for("list_dog"))

    return render_template("delete.html", form=form)


@app.route("/list")
def list_dog():
    all_dogs = Dog.query.all()  # Liste
    return render_template("list.html", dogs=all_dogs)


if __name__ == "__main__":
    app.run(debug=True)
