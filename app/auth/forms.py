from flask_wtf import FlaskForm

# inportation of input fields from
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, RadioField, TextAreaField

# importation of validators
from wtforms.validators import Required, Email, EqualTo

# custom validator
from wtforms import ValidationError

# import User model
from ..models import User
