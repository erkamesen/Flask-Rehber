from flask import Flask, render_template, request, redirect, url_for # Flask kısmı
from flask_wtf import FlaskForm # Inheritance alacağımız class
from wtforms import StringField, EmailField, SubmitField # Formlarımızı bu paketten çekiyoruz.

app = Flask(__name__) 


app.config["SECRET_KEY"] = "herhangibirsey" # CRF için belirliyoruz.

class ContactForm(FlaskForm):
    name = StringField("İsim")
    email = EmailField("Email")
    msg = StringField("Mesaj")
    submit = SubmitField("Yolla")


@app.route("/", methods=["GET","POST"])
def index():
    form = ContactForm()
    if request.method == "POST":
        isim = request.form.get("name", "bilinmiyor")
        email = request.form.get("email", "email girilmedi")
        mesaj = request.form.get("msg", "mesaj girilmedi")
        with open("veritabani.txt", "a") as f:
            f.write(f"isim: {isim}, email: {email}, mesaj: {mesaj}")
        return redirect(url_for("index"))
    return render_template("index.html", form=form)