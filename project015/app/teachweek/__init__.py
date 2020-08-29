from flask import Blueprint

teachweek = Blueprint('teachweek', __name__)

from . import views
