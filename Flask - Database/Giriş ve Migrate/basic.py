import os # Database imizi oluşturcağımız klasörü belirtmek için.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask-Migrate

# Projemizim bulunduğu dizinin path ini alalım
basedir = os.path.abspath(os.path.dirname(__file__))
# /home/erkam/Files/Flask/Flask-Rehber/Flask - Database

# Uygulamamızı oluşturalım
app = Flask(__name__)


# Config Ayarlarını yapalım.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy nesnemizi oluşturup uygulamamızda initialize edelim
db = SQLAlchemy(app=app)

# Migrate nesnemizi oluşturalım ve bağlantıyı sağlayalım
Migrate(app, db)

###################################
""" MODEL OLUŞTURMA """

# db.Model classından miras alıyoruz
class Dog(db.Model):

    # Opsiyonel: Tablo ismini belirtiyoruz.Eğer belirtmezsek sınıf ismi tablo ismi oluyor.
    __tablename__ = "dogs"

    # Kolonları oluşturma
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    #migration için yeni bir kolon oluşturuyoruz.
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Debug kısmında kullanmak için.
    def __repr__(self):
        return f"Dog {self.name} is {self.age} year's old."
