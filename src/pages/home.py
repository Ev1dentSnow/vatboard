from flask import Blueprint, render_template, current_app as app, abort, session
import requests
import json
import uuid

page = Blueprint('home', __name__, template_folder='../templates/')

@page.route('/')
@page.route('/home')
def home():
    vatsim_auth = session.get('vatsim_auth_res', None)
    if vatsim_auth != None:
        data = api_req(vatsim_auth['access_token'])
        populate_session(data)
    try:
        return render_template('index.html')
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

def populate_session(data):
    session['cid'] = data['data']['cid']
    session['auth_token'] = f"{uuid.uuid4()}/{session['cid']}"
    session['vatsim_data'] = data['data']
    session['first_name'] = data['data']['personal']['name_first']
    session['last_name'] = data['data']['personal']['name_last']

