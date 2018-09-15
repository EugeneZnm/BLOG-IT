# importing db
from . import db
# security model providing haching functionality
from werkzeug.security import generate_password_hash, check_password_hash

# import class UserMixin
from flask_login import UserMixin

# import login manager
from . import login_manager

from datetime import datetime


class Writer(UserMixin, db.Model):
    """
    creating class writer for creating blog writer and connecting it to database via db.Model

    """
    __tablename__ = 'writer'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))

    # call  back function retrieving writer id
    @login_manager.writer_loader
    def load_writer(writer_id):
        return Writer.query.get(int(writer_id))

    def set_password(self, password):
        """
        method to set passwords
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        method to verify password
        """
        return check_password_hash(self.pass_secure, password)

    def  __repr__(self):
        return f'Writer {self.username}'




