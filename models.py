from flask_login import UserMixin
from datetime import datetime
from .app import db 
class Books(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_book = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable = False)
    year= db.Column(db.Date, nullable=True, default=datetime.utcnow)
    value_book = db.Column(db.Integer, nullable = False)
class Issue_log(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_log = db.Column(db.Date, nullable=True, default=datetime.utcnow)
    user_log = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
    book_log = db.Column(db.Integer, db.ForeignKey('books.id'),nullable = False)
    status_log = db.Column(db.Integer, db.ForeignKey('status.id'),nullable = False)
class Status(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255) , nullable=False)
class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(32), nullable = False)
    user_pass = db.Column(db.String(32), nullable=False)
    user_fio = db.Column(db.String(255),nullable = False)
    user_role = db.Column(db.Integer, db.ForeignKey('role.id'),nullable = False)
class Role(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(32), nullable=False)
    role_description = db.Column(db.Text , nullable=False)