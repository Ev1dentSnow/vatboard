from flask import Blueprint, render_template, current_app as app

page = Blueprint('server_error', __name__, template_folder='../templates/')

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500