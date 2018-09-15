from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField, TextField

from wtforms.validators import Required


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    saying = TextAreaField('Write your comment')
    submit = SubmitField('Submit')


