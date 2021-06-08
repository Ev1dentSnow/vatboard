from flask import Blueprint, redirect, current_app as app

auth_module = Blueprint('login', __name__)

@auth_module.route('/login')
def login():
    return redirect(app.config['AUTH_URL'])