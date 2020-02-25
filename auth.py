from flask import Blueprint , render_template , redirect , url_for , request , flash 
from werkzeug.security import generate_password_hash , check_password_hash
from .app import db
from flask_login import login_required , current_user , login_user ,logout_user

import re

auth = Blueprint('auth',__name__)
