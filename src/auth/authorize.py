from flask import Blueprint, redirect, request, url_for, current_app as app, session
import requests
import json

auth_module = Blueprint('authorize', __name__)

@auth_module.route('/authorize')
def authorize():
    error = request.args.get('error')
    if error:
        return "You rejected the auth attempt."
    code = request.args.get('code')
    if code == None:
        return "Something went wrong."

    body = build_token_post(code)
    post_req = requests.post(app.config['TOKEN_URL'], body)
    res = json.loads(post_req.text)

    try:
        session['vatsim_auth_res'] = res
    except:
        return "Redis connection not made."

    return redirect('/')

def build_token_post(code):
    body = {
        'grant_type': 'authorization_code',
        'client_id': app.config['CLIENT_ID'],
        'client_secret': app.config['CLIENT_SECRET'],
        'redirect_uri': app.config['REDIRECT_URL'],
        'code': code
    }
    return body