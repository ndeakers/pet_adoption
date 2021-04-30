from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[InputRequired(),
                                                     URL()])
    age = SelectField("Age", choices=[("baby", "Baby"), 
                                      ("young", "Young"),
                                      ("adult", "Adult"),
                                      ("senior", "Senior")])
    notes = StringField("Notes")
