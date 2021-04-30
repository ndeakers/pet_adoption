from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("dog", "Dog"),
                                              ("cat", "Cat"),
                                              ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(),
                                                     URL()])
    age = SelectField("Age", choices=[("baby", "Baby"),
                                      ("young", "Young"),
                                      ("adult", "Adult"),
                                      ("senior", "Senior")])
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing pet information"""
    photo_url = StringField("Photo URL", validators=[Optional(),
                                                     URL()])
    notes = StringField("Notes")
    available = BooleanField("Available")
