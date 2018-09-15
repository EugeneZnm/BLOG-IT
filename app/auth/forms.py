from flask_wtf import FlaskForm

# inportation of input fields from
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, RadioField, TextAreaField

# importation of validators
from wtforms.validators import Required, Email, EqualTo

# custom validator
from wtforms import ValidationError

# import User model
from ..models import User


class RegistrationForm(FlaskForm):
    """
    registration form class for creation of input fields

    """
    email = StringField('Input Email Address', validators=[Required(), Email()])
    username = StringField('Input username', validators=[Required()])
    password = PasswordField('Password',validators=[Required(), EqualTo('password', message='Passwords must match')])
    password_second = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('SIGN UP')

    def validate_email(self, data_field):
        """
        Method to checking if email used matches existing emails

        """
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email matches existing account')

    def validate_username(self, data_field):
        """
        checking if username keyed in matches existing usernames

        """
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('Username is already Taken, try another one')
