#!/bin/bash

# Check requirements
check=$(pip freeze | grep 'Flask\|numpy\|pandas')
[[ $check != *"Flask=="* ]] && pip install Flask
[[ $check != *"Flask-RESTful=="* ]] && pip install flask-restful
[[ $check != *"numpy=="* ]] && pip install numpy
[[ $check != *"pandas=="* ]] && pip install pandas

export FLASK_APP=app.py
[[ $1 == "dev" ]] && export FLASK_ENV=development
flask run