from flask import Blueprint , render_template , url_for , redirect , request

from flask_login import current_user
from .app import db
import datetime

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')