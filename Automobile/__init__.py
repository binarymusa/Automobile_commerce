from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from instance.config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_session import Session

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

session =  Session(app)
api = Api(app)

app.app_context().push()

from  Automobile import views