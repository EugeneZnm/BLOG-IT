from flask import Blueprint

# creating a blueprint instance
auth = Blueprint('auth', __name__)

from . import views, forms