"""
Example file for local_settings.py

Copy this specific file an rename it to local_settings.py with
the correct settings for your local environment.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hivemind',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME_ZONE = 'UTC+3'
