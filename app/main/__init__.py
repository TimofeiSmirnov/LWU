from flask import Blueprint

mn = Blueprint('main', __name__)

from app.main import routes

