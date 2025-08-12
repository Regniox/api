#!/usr/bin/bash

set -e

python -m venv venv
. venv/bin/activate

./venv/bin/pip install --upgrade pip

./venv/bin/pip install -r requirements.txt