from flask import Blueprint, render_template, url_for, redirect, flash
from myproject.owners.forms import AddForm
from myproject.models import Owner, Dog
from myproject import db

owner = Blueprint("owner", __name__, template_folder="templates/owners", url_prefix="/owner")


@owner.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        dog = Dog.query.get(id)
        if dog.owner:
            flash("Üzgünüz bu köpegin zaten bir sahibi mevcut :/ Lütfen baska bir tane seciniz.")
            return redirect(url_for("owner.add"))
        
        new_owner = Owner(name, id)       
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("dog.  list_dog"))
    return render_template("add.html", form=form)
