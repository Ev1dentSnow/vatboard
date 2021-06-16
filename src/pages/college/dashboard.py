from flask import Blueprint, render_template, abort, session

page = Blueprint('/dashboard', __name__, template_folder='../../templates/college/')

@page.route('/college')
@page.route('/college/dashboard')
def dashboard():
    if session.get('auth_token', None) == None:
        abort(401)
    try:
        populate_session()
        print("done")
        return render_template('dashboard.html')
    except:
        abort(404)



def populate_session():
    return ''