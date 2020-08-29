from flask import Blueprint

error = Blueprint('error', __name__)

from . import views
