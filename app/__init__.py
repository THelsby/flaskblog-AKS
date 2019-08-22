from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flaskblogdb'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes, models

tables = db.engine.table_names()
try:
    tables.remove('alembic_version')
except ValueError:
    pass

if len(tables) == 0:
    db.create_all()
    db.session.commit()
    print("Database tables not initialized")







