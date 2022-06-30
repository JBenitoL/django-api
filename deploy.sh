#!/bin/bash
export WORKSPACE=`pwd`
# Create/Activate virtualenv
virtualenv venv
source venv/bin/activate
# Install Requirements
pip install -r requirements.txt
# Run tests
python manage.py makemigrations
python manage.py migrate
python manage.py test