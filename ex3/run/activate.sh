#!/bin/bash

# Create virtual environment if directory doesn't exist yet
if [ ! -d "./venv" ]
then
	sudo apt install python3-venv
	python3 -m venv venv
fi

# Activate virtual environment
[[ "$VIRTUAL_ENV" == "" ]] && source venv/bin/activate