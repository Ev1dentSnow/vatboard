from flask import Blueprint, render_template, abort, session

page = Blueprint('/profile', __name__, template_folder='../../templates/college/')

@page.route('/college/profile')
def profile():
    if session.get('auth_token', None) == None:
        abort(401)
    try:
        populate_session()
        return render_template('profile.html')
    except:
        abort(404)



def populate_session():
    data = session['vatsim_data']
    session['atc_rating_id'] = data['vatsim']['rating']['short']
    session['email'] = data['personal']['email']
    session['home_country'] = data['personal']['country']['name']
    session['home_country_id'] = data['personal']['country']['id']

    session['atc_rating_name'] = data['vatsim']['rating']['long']
    session['region_name'] = data['vatsim']['region']['name']
    session['region_id'] = data['vatsim']['region']['id']
    session['division_name'] = data['vatsim']['division']['name']
    session['division_id'] = data['vatsim']['division']['id']
    session['vacc_name'] = data['vatsim']['subdivision']['name']
    session['vacc_id'] = data['vatsim']['subdivision']['id']
    session['pilot_rating_name'] = data['vatsim']['pilotrating']['long']
    session['pilot_rating_short'] = data['vatsim']['pilotrating']['short']