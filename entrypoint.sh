#!/bin/sh

python manage.py makemigrations
python manage.py migrate



gunicorn -b 0.0.0.0 -p 8000 Ntk_blog-master.wsgi:application