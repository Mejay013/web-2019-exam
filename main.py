from flask import Blueprint , render_template , url_for , redirect , request
from .models import Books,Issue_log,Status,User,Role
from flask_login import current_user
from .app import db
import datetime

main = Blueprint('main',__name__)

@main.route('/')
def index():
    books_list = Books.query.order_by(Books.author.desc())
    issue_list = Issue_log
    status_list = Status
    user = User
    role = Role
    return render_template('index.html',books_list=books_list,issue_list=issue_list,status_list=status_list,user=user,role=role)
