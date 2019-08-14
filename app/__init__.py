from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from app import routes, models




