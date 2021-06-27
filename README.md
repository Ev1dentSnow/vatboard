# VATSIM SSO in Python using Flask

This is an implementation of VATSIM's SSO client in Python.

## Requirements

To install requirements, run `pip install <requirement>`.

Requirements:

- Flask
- Redis
- Flask-Session
- Requests

It is recommended that you set up a virtual environment before installing the packages.

A Redis docker instance is required. To get this up and running, ensure docker is installed and running. Next, open a terminal and run `docker run --name flask-app -p 6379:6379 -d redis`.
More on Redis can be found on the [docker page](https://hub.docker.com/_/redis).

## Running

To run, move into the `src` directory and run `export FLASK_APP=run.py` for Bash or `set FLASK_APP=run.py` for Windows.
Next run `flask run` and the app will start on port 5000.

## Deployment

Flask's built in WSGI is not suitable for production as it doesn’t scale well. 

A good production ready WSGI is gunicorn, available here: https://gunicorn.org

Gunicorn is built to be run behind a reverse proxy such as NGINX. For more on deploying a flask app with Gunicorn and NGINX on Ubuntu, see this guide: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04 

## VATSIM Documentation

Please visit [this website](https://forums.vatsim.net/topic/26902-new-sso-vatsim-connect-update/) for documentation on VATIM's SSO system.
