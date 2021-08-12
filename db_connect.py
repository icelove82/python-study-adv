import inspect

import mysql.connector as dbc

print(dir(dbc))
print(inspect.getfile(dbc))

db = dbc.connect(
    host='localhost',
    user='develop',
    password='develop',
    database='study'
)


def do_db_connect():
    return db
