from mysql.connector import connect
from flask import g


def init_app(app):
    app.teardown_appcontext(close_connection)


def get_connection():
    if 'connection' not in g:
        g.connection = connect(db='appmy', user='app', password='app123', host='db')

    return g.connection


def close_connection():
    connection = g.pop('connection', None)

    if connection is not None:
        connection.close()