from flask_login import login_required, current_user

from flask import render_template, redirect, request, url_for, abort

from ..models import Post, Comments

from . import main

from .forms import BlogForm, CommentForm

# import photos instance
from .. import db

import markdown2


@main.route('/')
def index():

    title = 'MOMENT OF TRUTH'
    all = Post.query.all()
    return render_template('index.html',all=all, title=title)


# display blog and blog categories
@main.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    """
    function to display pitch form
    """
    posts = BlogForm()

    if posts.validate_on_submit():

        posted = Post(post=posts.pitch.data, category=posts.category.data)
        posted.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new-pitch.html',post=posts)


# display comments
@main.route('/comments/<int:id>', methods = ['GET', 'POST'])
def comments(id):
    """
    show comments
    """
    comment = CommentForm()
    comment_is = Comments.query.filter_by(pitch_id=id)
    if comment.validate_on_submit():

        comments = Comments(saying=comment.saying.data,pitch_id=id, user_id=current_user.id )
        comments.save_comments()
        comment_is= Comments.query.filter_by(pitch_id=id)
        return render_template('comments.html', comment=comment, comment_is=comment_is)

    return render_template('comments.html', comment=comment, comment_is=comment_is)