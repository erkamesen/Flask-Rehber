from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegisterForm
from flask_migrate import Migrate



Migrate(app, db)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/welcome")
@login_required
def welcome():
    return render_template("welcome_user.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        print(user.username)
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Giriş Yapildi!!!")

            next = request.args.get("next")
            print(next)
            if next == None or not next[0]=="/":
                next = url_for("welcome")
            
            return redirect(next)

    else:
        return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Cikis Yapildi!")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(form.email.data, form.username.data, form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Kayit Olundu.!!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)