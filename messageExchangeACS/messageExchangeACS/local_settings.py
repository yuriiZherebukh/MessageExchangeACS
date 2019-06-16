"""
This module contains local configurations for MessageExchangeACS project
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'MessageExchangeACS',
        'USER': 'postgres',
        'PASSWORD': 'qweqwe',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
