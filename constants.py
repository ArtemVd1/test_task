import os


HOST = 'localhost'
PSQL_USER = os.environ.get('PSQL_USER')
PSQL_PASSWORD = os.environ.get('PSQL_PASSWORD')
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

