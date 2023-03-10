from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

db= SQLAlchemy()
migrate= Migrate()
login_manager = LoginManager() 


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)
login_manager.init_app(app)

# from app import routes, models
from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)

from app.blueprints.main2 import bp as main2_bp
app.register_blueprint(main2_bp)

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)




