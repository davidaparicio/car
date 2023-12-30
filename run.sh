#!/usr/bin/env bash

export FLASK_APP=app
export FLASK_ENV=development
#python run.py
flask --app ${FLASK_APP} run --debug
#export FLASK_ENV=production
#flask run --host=0.0.0.0
