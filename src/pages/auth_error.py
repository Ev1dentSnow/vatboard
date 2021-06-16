from flask import Blueprint, render_template, current_app as app

page = Blueprint('auth_error', __name__, template_folder='../templates/')

@app.errorhandler(401)
def auth_error(e):
    return render_template('401.html'), 401