"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name",
                       validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = URLField('Photo URL',
                          validators=[Optional(),URL()])
    age = StringField("Age",
                      validators=[InputRequired(), AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes= TextAreaField("Notes",
                         validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pet information. """

    photo_url = URLField('Photo URL',
                          validators=[URL()])
    age = StringField("Age",
                      validators=[InputRequired(), AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes= TextAreaField("Notes",
                         validators=[Optional()])