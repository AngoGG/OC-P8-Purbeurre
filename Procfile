release: python manage.py migrate && python manage.py fill_database

web: gunicorn config.wsgi --log-file -