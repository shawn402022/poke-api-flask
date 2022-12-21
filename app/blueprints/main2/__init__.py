from flask import Blueprint

bp = Blueprint('main2', __name__, url_prefix='/main2')

from . import routes,models