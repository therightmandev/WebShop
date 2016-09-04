import sys, os

EMAIL = os.environ.get('FLASK_EMAIL', '')
EMAIL_PASSWORD = os.environ.get('FLASK_EMAIL_PASSWORD', '')
DB_PATH = 'sqlite:///test.db'

if EMAIL == '' or EMAIL_PASSWORD == '':
    sys.exit('Please write email and password in server/config.py')
