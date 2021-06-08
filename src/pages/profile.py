from flask import Blueprint, render_template, abort, session, redirect

page = Blueprint('profile', __name__, template_folder='../templates/')

@page.route('/profile')
def profile():
    if session.get('first_name', None) == None:
        return redirect('/')
    return render_template('profile.html')