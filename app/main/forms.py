from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField, TextField

from wtforms.validators import Required, Email, EqualTo


class CommentForm(FlaskForm):
    """
    class to create comment form
    """
    name = StringField('Your Name')
    comment = TextField('Write your comment')
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    """
    class to create blog post form
    """
    title = StringField('Blog post title')
    post = TextAreaField('Blog Content')
    category = RadioField('Categories', choices = [('lifestyle', 'lifestyle'),('Business', 'Business'),('Entertainment', 'Entertainment'), ('Culture','Culture')],validators=[Required()])
    submit = SubmitField('Submit')