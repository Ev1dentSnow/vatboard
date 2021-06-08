from flask import Blueprint, render_template, current_app as app, abort, session
import requests

page = Blueprint('home', __name__, template_folder='../templates/')

@page.route('/')
@page.route('/home')
def home():
    vatsim_auth = session.get('vatsim_auth_res', None)
    if vatsim_auth != None:
        data = api_req(vatsim_auth['access_token'])
        session['vatsim_data'] = data['data']
        session['name'] = data['data']['personal']['name_full']
    try:
        return render_template('home.html')
    except:
        abort(404)

def api_req(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    try:
        data = requests.get(app.config['API_URL'], headers=headers).json()
        return data
    except Exception as ex:
        print(f"Exception: {ex}")
        return None