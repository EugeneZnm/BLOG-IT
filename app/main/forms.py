from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField, TextField


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    name = StringField('Your Name')
    comment = TextAreaField('Write your comment')
    submit = SubmitField('Submit')


