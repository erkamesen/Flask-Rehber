# MODELS.py
# db yi __init__.py içinde oluşturucaz.
from myproject import db


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
