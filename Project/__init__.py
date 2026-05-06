from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager
def create_app():
    global app
    global db
    global loginmanager
    
    app = Flask(__name__)

    app.config['SECRET_KEY']='secret'
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    db = SQLAlchemy(app)
    Migrate(app,db)    

    loginmanager = LoginManager(app)
    loginmanager.login_view='login'

    from Project.home import bp as homebp
    from Project.auth import bp as authbp
    from Project.tables import bp as tablebp
    app.register_blueprint(homebp)
    app.register_blueprint(authbp,url_prefix='/auth')
    app.register_blueprint(tablebp,url_prefix='/tables')
    return app

