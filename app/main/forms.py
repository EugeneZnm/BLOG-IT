from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField, TextField

from wtforms.validators import Required


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    saying = TextAreaField('Write your comment')
    submit = SubmitField('Submit')


class Blog(FlaskForm):
    """
    class to create blog post form
    """
    pitch = TextAreaField('Pitch Goes Here')
    category = RadioField('Categories', choices = [('lifestyle', 'lifestyle'),('Business', 'Business'),('Entertainment', 'Entertainment'), ('Motivational','Motivational')],validators=[Required()])
    submit = SubmitField('Submit')