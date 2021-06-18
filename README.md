# VATBoard

A hub for managing members of a vACC or Division on the VATSIM Network.

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

## Env File

An environment (.env) will need to be created in the `/src/` folder. The structure should look something like this:

```sh
auth
pages
templates
.env
config.py
run.py
```

See the `example_env.md` file for an example .env file.

## Running

To run, move into the `src` directory and run `export FLASK_APP=run.py` for Bash or `set FLASK_APP=run.py` for Windows.
Next run `flask run` and the app will start on port 5000.

## VATSIM Documentation

Please visit [this website](https://forums.vatsim.net/topic/26902-new-sso-vatsim-connect-update/) for documentation on VATIM's SSO system.
