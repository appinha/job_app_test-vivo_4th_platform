#!/bin/bash

## Script for running in venv

# Check requirements
check=$(pip freeze)
requirements='requirements.txt'
while read line; do
	[[ $check != *"$line"* ]] && pip install $line
done < $requirements

# Run Flask application
PYTHONPATH=./ FLASK_ENV=development python3 ./api/app.py
