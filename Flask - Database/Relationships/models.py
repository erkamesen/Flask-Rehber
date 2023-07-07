import os  # Database oluşturulacak klasörü belirtmek için
from flask import Flask  # Uygulamayı oluşturmak için
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
# /home/erkam/Files/Flask/Flask-Rehber/Flask - Database/Relationships


# Uygulamayı Oluşturma
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy Oluşturma
db = SQLAlchemy(app)

# Migrate Oluşturma
Migrate(app, db)

""" MODELS """


class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # One to Many
    # 1 Köpek birden fazla oyuncağa sahip olabilir.
    # Liste şeklinde dönücek
    toys = db.relationship("Toy", backref="dog", lazy="dynamic")

    # One to One
    # 1 köpeğin 1 sahibi vardır.
    # uselist parametresini 1One to One olduğu için veriyoruz.
    owner = db.relationship("Owner", backref="dog", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Köpegin adi {self.name} ve sahibinin adi {self.owner.name}"
        else:
            return f"Köpegin adi {self.name} ve henüz bir sahibi yok!"

    def oyuncak_sayisi(self):
        print("İste oyuncaklarimin Listesi:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = "toys"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    dog_id = db.Column(db.Integer, db.ForeignKey("dogs.id"))

    def __init__(self, item_name, dog_id):

        self.item_name = item_name
        self.dog_id = dog_id


class Owner(db.Model):

    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    dog_id = db.Column(db.Integer, db.ForeignKey("dogs.id"))

    def __init__(self, name, dog_id):
        self.name = name
        self.dog_id = dog_id
