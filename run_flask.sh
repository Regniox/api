#!/usr/bin/bash

. venv/bin/activate
export FLASK_APP=api/app.py
export FLASK_ENV=development
flask run --host=0.0.0.0