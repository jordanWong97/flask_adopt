"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                        choices = [('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')],
                        validators=[InputRequired()])
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