from flask.ext.wtf import Form
from .models import User
from Pronounce import db
from wtforms import StringField, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, BooleanField

class DetailsForm(Form):
    """description of class"""


