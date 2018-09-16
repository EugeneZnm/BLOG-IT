from flask import render_template, url_for, redirect, request, flash
from . import auth
from flask_login import login_user, login_required, logout_user
# imoort user model
from ..models import User, Post
from .forms import RegistrationForm, LoginForm
from .. import db
# from ..email import mail_message


# view function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    login function to render template file
    :return:
    """
    login_form=LoginForm() # instance of Login form passed into login template
    if login_form.validate_on_submit():
        """
        checking form validation
        """
        user=User.query.filter_by(email = login_form.email.data).first()
        """
        searching for user in database with email received from form
        """
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitches login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/register', methods=['GET','POST'])
def register():
    """
    function to render registration form
    :return:
    """
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        title = "Welcome New User"
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form=form)


# logout route to logout user from application
@auth.route('/logout')
@login_required
def logout():
    """
    function to logout user
    :return:
    """
    logout_user()
    return redirect(url_for("main.index"))


