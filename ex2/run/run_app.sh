#!/bin/bash

## Script for running in venv

# Check requirements
check=$(pip freeze)
requirements='requirements.txt'
while read line; do
	[[ $check != *"$line"* ]] && pip install $line
done < $requirements

# Run Flask application
export FLASK_APP=app.py
[[ $1 == "dev" ]] && export FLASK_ENV=development
flask run