from flask import Blueprint

teachplan = Blueprint('teachplan', __name__)

from . import views
