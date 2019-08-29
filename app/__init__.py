from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os, time, pymysql

app = Flask(__name__)
app.config.from_object(Config)
if os.environ.get('DB_CONT_NAME') is None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flaskblogdb'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@%s:3306/flaskblogdb' % os.environ.get('DB_CONT_NAME')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes, models


retries = 128

for x in range(retries):
    try:
        tables = db.engine.table_names()
        break
    except Exception as exc:
        print(exc)
        if x < retries - 1:
            print("DB connection failed, retrying...")
            time.sleep(1)
        else:
            print("Error connecting to DB after ", retries, " retries")
            exit()

try:
    tables.remove('alembic_version')
except ValueError:
    pass

if len(tables) == 0:
    db.create_all()
    db.session.commit()
    print("Database tables not initialized")







