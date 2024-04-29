#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

# python manage.py makemigrations --merge
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username cworks --email ict.infrastructure@govt.lc --no-input
python manage.py collectstatic --no-input
python manage.py upload_data static/docs/INCOMING.xlsx
PYTHON manage.py add_outgoing_data static/docs/OUTGOING.xlsx


exec "$@"