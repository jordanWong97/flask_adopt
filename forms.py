"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, URLField

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = URLField('Photo URL')
    age = IntegerField("Species")
    notes= TextAreaField("Notes")