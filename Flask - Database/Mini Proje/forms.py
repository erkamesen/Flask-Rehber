from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Köpeğin Adi: ")
    submit = SubmitField("Köpek Ekle")


class DelForm(FlaskForm):

    id = IntegerField("Silinecek köpeğin ID si: ")
    submit = SubmitField("Köpek Sil")
