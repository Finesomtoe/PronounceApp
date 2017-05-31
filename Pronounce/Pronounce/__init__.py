"""
The flask application package.
"""
import os 
from flask import Flask
from flask import render_template
from flask.ext.mysql import MySQL
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail, Message
from threading import Thread

mysql = MySQL()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'home'
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'somtoskeyinwhichnobodycanguess'
app.config["MAIL_SERVER"] = "smtp.mail.yahoo.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'senendu5@yahoo.com'
app.config["MAIL_PASSWORD"] = ''
app.config['DIALECT_APP_SUBJECT'] = '[Dialect App]'
app.config['DIALECT_APP_SENDER'] = 'senendu5@yahoo.com'
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://limdialect_admin:OeOCMPSMn8NT7@mysql-limdialect.science.ru.nl/limdialect'#'mysql+pymysql://root:sokoamshe619+@localhost/testdb'
db = SQLAlchemy(app)
mail = Mail(app)

import Pronounce.views
