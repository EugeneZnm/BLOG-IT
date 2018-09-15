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


# Blog post categories
@main.route('/Lifestyle', methods = ['GET', 'POST'])
def promote():
    """
    displaying lifestyle blog post
    """
    lifestyle =Post.query.filter_by(category="Lifestyle").all()

    return render_template('lifestyle.html', post =lifestyle)


@main.route('/Business', methods = ['GET', 'POST'])
def product():
    """
    show business posts
    """
    business = Post.query.filter_by(category="business").all()

    return render_template('Business.html', post=business)


@main.route('/entertainment', methods = ['GET', 'POST'])
def entertainment():
    """
     show entertainment posts
    """
    entertainment = Post.query.filter_by(category="entertainment").all()

    return render_template('Entertainment.html', post=entertainment)


@main.route('/culture', methods = ['GET', 'POST'])
def culture():
    """
    show culture posts
    """
    culture = Post.query.filter_by(category='culture').all()

    return render_template('culture.html', post=culture)


# display comments
@main.route('/comments/<int:id>', methods = ['GET', 'POST'])
def comments(id):
    """
    show comments
    """
    comment = CommentForm()
    comment_is = Comments.query.filter_by(post_id=id)
    if comment.validate_on_submit():

        comments = Comments(comment=comment.saying.data,post_id=id)
        comments.save_comments()
        comment_is= Comments.query.filter_by(post_id=id)
        return render_template('comments.html', comment=comment, comment_is=comment_is)

    return render_template('comments.html', comment=comment, comment_is=comment_is)