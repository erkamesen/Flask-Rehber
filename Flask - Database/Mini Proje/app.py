from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from forms import AddForm, DelForm, AddOwnerForm


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
    owner = db.relationship("Owner", backref="dog", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"ID:{self.id} - Köpeğin ismi {self.name} ve sahibinin adi {self.owner.name}"
        else:
            return f"ID:{self.id} - Köpeğin ismi {self.name} ve henüz bir sahibi yok."


class Owner(db.Model):

    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    dog_id = db.Column(db.Integer, db.ForeignKey("dogs.id"))

    def __init__(self, name, dog_id):
        self.name = name
        self.dog_id = dog_id


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


@app.route("/add-owner", methods=["GET", "POST"])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        dog = Dog.query.get(id)
        if dog.owner:
            print("Geldi")
            flash("Üzgünüz bu köpegin zaten bir sahibi mevcut :/ Lütfen baska bir tane seciniz.")
            return redirect(url_for("add_owner"))
        
        new_owner = Owner(name, id)       
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("list_dog"))
    return render_template("owner.html", form=form)


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
