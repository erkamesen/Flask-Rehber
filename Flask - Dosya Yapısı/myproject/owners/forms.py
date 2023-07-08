# Owners için forms.py dosyası

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Sahibin Adi: ")
    id = IntegerField("köpeğin ID si: ")
    submit = SubmitField("Sahip Ekle")
