from config import Config
from flask import Flask
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config['REDIS_SECRET']
app.debug = True

SESSION_TYPE = 'redis'
Session(app)


with app.app_context():
    # auth
    from auth.login import auth_module as login
    from auth.logout import auth_module as logout
    from auth.authorize import auth_module as authorize

    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(authorize)

    # pages
    from pages.home import page as home
    from pages.college.profile import page as profile
    from pages.college.dashboard import page as dashboard

    app.register_blueprint(home)
    app.register_blueprint(profile)
    app.register_blueprint(dashboard)
