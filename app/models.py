  importing db
from . import db
# security model providing haching functionality
from werkzeug.security import generate_password_hash, check_password_hash

# import class UserMixin
from flask_login import UserMixin

# import login manager
from . import login_manager

from datetime import datetime