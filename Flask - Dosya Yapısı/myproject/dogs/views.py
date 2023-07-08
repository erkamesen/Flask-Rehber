from flask import Blueprint, render_template, url_for, redirect
from myproject.dogs.forms import AddForm, DelForm
from myproject.models import Dog
from myproject import db

dog = Blueprint("dog", __name__, template_folder="templates/dogs", url_prefix="/dog")



@dog.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_dog = Dog(name)
        db.session.add(new_dog)
        db.session.commit()

        return redirect(url_for("dog.list_dog"))
    return render_template("add.html", form=form)


@dog.route("/delete", methods=["GET", "POST"])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        dog = Dog.query.get(id)
        db.session.delete(dog)
        db.session.commit()
        return redirect(url_for("dog.list_dog"))

    return render_template("delete.html", form=form)


@dog.route("/list")
def list_dog():
    all_dogs = Dog.query.all()  # Liste
    return render_template("list.html", dogs=all_dogs)
