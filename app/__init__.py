from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_fontawesome import FontAwesome

admin = Admin()
mail = Mail()
simple = SimpleMDE()
fa = FontAwesome()
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'




def create_app(config_name):
    app = Flask(__name__)

    # Create app configurations
    app.config.from_object(config_options[config_name])
   

    #Initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    fa.init_app(app)

    #Registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    #Set requests config
    from .requests import configure_request
    configure_request(app)

    #Will add the views and forms
    return app
