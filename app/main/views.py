import markdown2
from flask import abort, flash, redirect, render_template, request, url_for,abort
from flask_login import current_user, login_required

from . import main
from .. import db, photos
from ..email import mail_message
from ..models import Comments, Post, Subscriber, User
from .forms import BlogForm, CommentForm, SubscriptionForm, UpdateProfile
from app.main.forms import UpdateProfile


@main.route('/', methods=['GET','POST'])
def index():
    title = 'MOMENT OF TRUTH'
    all = Post.query.order_by(Post.id.desc()).all()
    subscribed = SubscriptionForm()
    subscribers = Post.query.all()
    if subscribed.validate_on_submit():

        subscribers = Subscriber(email=subscribed.email.data,username = subscribed.username.data)
        db.session.add(subscribers)
        db.session.commit()
        mail_message("Welcome To Codex ","email/welcome-subscriber",subscribers.email,subscribers=subscribers)

    # search = BlogSearchForm(request.form)
    # if request.method == 'POST':
    #     return search_results(search)

    return render_template('index.html', all=all, title=title, subscribed=subscribed, subscribers=subscribers, post=post)


# display blog and blog categories
@main.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    """
    function to display pitch form
    """
    posts = BlogForm()
    postit = Post.query.all()
    
    if posts.validate_on_submit():
        posted = Post(post=posts.post.data, category=posts.category.data, header=posts.header.data)
        posted.save_post()
        return redirect(url_for('main.index'))

    subscribers = Subscriber.query.all()
    for email in subscribers:
        mail_message("New Blog Post from Codex ","email/postnotification",email.email,subscribers=subscribers)
    
    return render_template('blog-post.html', posts=posts, postit=postit)

# Blog post categories
@main.route('/Lifestyle', methods=['GET', 'POST'])
def lifestyle():
    """
    displaying lifestyle blog post
    """
    lifestyle = Post.query.filter_by(category="lifestyle").all()

    return render_template('lifestyle.html', post=lifestyle)


@main.route('/Business', methods=['GET', 'POST'])
def business():
    """
    show business posts
    """
    business = Post.query.filter_by(category="Business").all()

    return render_template('business.html', post=business)


@main.route('/entertainment', methods=['GET', 'POST'])
def entertainment():
    """
     show entertainment posts
    """
    entertainment = Post.query.filter_by(category="Entertainment").all()

    return render_template('entertainment.html', post=entertainment)


@main.route('/culture', methods=['GET', 'POST'])
def culture():
    """
    show culture posts
    """
    culture = Post.query.filter_by(category='culture').all()

    return render_template('culture.html', post=culture)


# display comments
@main.route('/comments/<int:id>', methods=['GET', 'POST'])
def comments(id):
    """
    show comments
    """
    comment = CommentForm()
    comment_is = Comments.query.filter_by(post_id=id)
    if comment.validate_on_submit():
        comments = Comments(comment=comment.comment.data, post_id=id, name=comment.name.data)
        comments.save_comments()

    postit = Post.query.all()

    return render_template('comments.html', comment=comment, comment_is=comment_is, postit=postit)


# # reader subscription form
# @main.route('/subscribed', methods=['GET','POST'])
# def subscriber():
#     """
#      function to subscribe readers to blog
#     """
#     subscribed = SubscriptionForm()

#     if subscribed.validate_on_submit():

#         subscribers = Subscriber(email=subscribed.email.data,username = subscribed.username.data)
#         db.session.add(subscribers)
#         db.session.commit()
#         mail_message("Welcome To Codex ","email/welcome-subscriber",subscribed.email,subscriber=subscriber)

#         subscribers = Post.query.all()
#         post = Post.query.all()

#         return redirect(url_for('main.index'))

#     return render_template('subscribed.html',subscribed=subscribed, subscribers=subscribers, post=post)


# deletion of blog post
@main.route('/delete/<id>')
@login_required
def deletepost(id):

    """
     function to delete our blog post
    """
    post = Post.query.filter_by(id=id).first()

    post.delete_post()
    return redirect(url_for('main.index'))


# deletion of blog post
@main.route('/deletes/<id>')
def deletecomment(id):

    """
     function to delete our comment
    """
    comment = Comments.query.filter_by(id=id).first()

    comment.delete_comments()
    return redirect(url_for('main.index'))    

@main.route('/posts/<int:id>', methods=['GET', 'POST'])
def single_pitch(id):
    view = Post.query.filter_by(id=id)

    comment = CommentForm()
    comment_is = Comments.query.filter_by(post_id=id)
    if comment.validate_on_submit():
        comments = Comments(comment=comment.comment.data, post_id=id, name=comment.name.data)
        comments.save_comments()
   
    return render_template('singleblog.html', comment=comment, comment_is=comment_is,view=view)


# # search function
# @app.route('/results')
# def search_results(search):
#     results=[]
#     search_string = search.data['search']


#     #  search for blog post
#     if search.data['search'] == '':
#         qry = db.session.query(Post)
#         results = qry.all()

#     # prompt results are found    
#     if not results:
#         flash('No Results Found')
#         return redirect(url_for('main.index'))      
    
#     else:
#         #display results
#         table = Results(results)
#         table.border = True
#         return render_template('results.html', table=table)


# user profile
@main.route('/user/<uname>')
def profile(uname):
    """
    profile name function
    :param uname:
    :return:
    """
    user = User.query.filter_by(username = uname).first()
    """
    querying database to find user according to username passed
    """
    if user is None:
        """
        calling abort if no user is found
        """
        abort(404)

    # template rendering when user is found and passing in of user a a variable
    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    """
    function to take in username and instantiates the UpdateProfile class
    :param uname:
    :return:
    """
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        """
        validate content of user.bio to fill in what user has submitted
        """
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        # redirecting user back to login page
        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form =form)


# route processing form submission request accepting only post requests
@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    """
    querying database to pick user with username passed in
    """
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        """
        request function to check in any parameter with name photo passed into request
        save method to save file into application
        """
        path = f'photos/{filename}'
        user.profile_pic_path = path
        """
        update profile pic path property in user table and store path to the file
        """
        db.session.commit()
        """
        committing changes to database and redirect user to profile page
        """
    return redirect(url_for('main.profile', uname=uname))
