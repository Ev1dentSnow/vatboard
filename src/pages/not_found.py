from flask import Blueprint, render_template, current_app as app

page = Blueprint('not_found', __name__, template_folder='../templates/')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404