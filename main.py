from flask import Blueprint , render_template , url_for , redirect , request
from .models import Books,Issue_log,Status,User,Role
from flask_login import current_user
from .app import db
import datetime

main = Blueprint('main',__name__)

@main.route('/')
def index():
    books_list = Books.query.order_by(Books.author.desc())
    return render_template('index.html',books_list=books_list)

@main.route('/issue')
def issue():
    books_list = Books
    issue_list = Issue_log.query.order_by(Issue_log.date_log.desc())
    status_list = Status
    user = User
    role = Role
    return render_template('issue.html',books_list=books_list,issue_list=issue_list,status_list=status_list,user=user,role=role)

@main.route('/set/<id>',methods=['POST','GET'])
def set(id):
    if request.method == 'POST':
        bad_issue= Issue_log.query.filter_by(id=id).first()

        if not bad_issue:
            books_list = Books
            issue_list = Issue_log.query.order_by(Issue_log.date_log.desc())
            status_list = Status
            user = User
            role = Role
            error = "Изменения уже приступили в силу"
            return render_template('issue.html',books_list=books_list,issue_list=issue_list,status_list=status_list,user=user,role=role,error = error)


        new_date = bad_issue.date_log
        new_book = bad_issue.book_log

        user_id = request.form['new_user_issue']
        new_status = request.form['new_status']

        db.session.delete(bad_issue)
        new_issue = Issue_log(date_log=new_date , user_log=user_id ,book_log=new_book,status_log=new_status )
        db.session.add(new_issue)
        db.session.commit()
        return render_template('index.html')
    else:
        issue = Issue_log.query.filter_by(id = id).first()
        books_list = Books
        status_list = Status.query.all()
        status = Status
        user = User
        user_list = User.query.all()
        role = Role
        return render_template('set.html',books_list=books_list,issue=issue,status_list=status_list,user=user,role=role,user_list=user_list)
