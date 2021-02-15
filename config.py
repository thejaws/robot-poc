### config.py ###
import os


class Config(object):
    THOR_API_KEY = os.environ.get('THOR_API_KEY') or 'you-will-never-guess-jawsrulz'
    ACE_API_BASE = os.environ.get('ACE_API_BASE') or 'not set api'
    EVENTS_API_BASE = os.environ.get('EVENTS_API_BASE') or 'not set events api'
# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
