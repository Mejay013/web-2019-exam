from flask import Flask 
from flask_login import LoginManager ,UserMixin
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

app = Flask(__name__)
application = app

app.config["SECRET_KEY"] = '_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)
from .models import User

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

## sudo tail -f /opt/unit/unit.log
## sudo sv restart unit
## . ve/bin/activate
## https://www.sinyawskiy.ru/sqlalchemy.html
## https://regex101.com
## INSERT INTO books (name_book, author,value_book) VALUES ('Дети капитана Гранта','Жуль Верн',30),('2000 лье под водой','Жуль Верн',15),('История России','Анастасия Михалова',120),('Веб-разработка для самых маленьких','Зигмунд Фрейд',20);
## DELETE FROM users WHERE id > 5; | or| TRUNCATE users;
## SELECT `id`,`name` FROM `users` WHERE `id`>3 AND `id` <5
##INSERT INTO appeal_type (type_appeal) VALUES ('Проблемы с компьютером');
##INSERT INTO appeal_type (type_appeal) VALUES ('Доступ в интернет'),('Доступ к общим ресурсам организации'),('Предоставление доступа'),('Другое');
##INSERT INTO appeal_status (status_appeal) VALUES ('Новое'),('В работе'),('Ошибочное'),('Отказано'),('Решено');
##INSERT INTO role (role , description) VALUES ('администратор','суперпользователь, имеет полный доступ к системе, в том числе к удалению обращений'),('специалист технической поддержки','может производить манипуляции с состоянием обращений — изменением статуса'),('пользователь','может оставлять обращения');
##
##
