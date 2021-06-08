from flask import Blueprint, redirect, url_for, session

auth_module = Blueprint('logout', __name__)

@auth_module.route('/logout')
def logout():
    session.clear()
    return redirect('/')