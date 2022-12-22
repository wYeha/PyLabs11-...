#!/usr/bin/env python3
import cgi
import html
import sqlite3
import os
form = cgi.FieldStorage()
def check_db(filename):
    return os.path.exists(filename)
db_file = 'database.db'
schema_file = 'schema.sql'
name = form.getfirst("in_name", "не задано")
car = form.getfirst("in_car", "не задано")
watchmen = form.getfirst("in_watchmen", "не задано")
arrivaLog = form.getfirst("in_arrivaLog", "не задано")
departureLog = form.getfirst("in_departureLog", "не задано")
name = html.escape(name)
car = html.escape(car)
watchmen = html.escape(watchmen)
arrivaLog = html.escape(arrivaLog)
departureLog = html.escape(departureLog)
dataforms = (name, car, watchmen, arrivaLog, departureLog)
if check_db(db_file):
    print('Database already exists. Exiting...')
with open(schema_file, 'r') as rf:
    schema = rf.read()

with sqlite3.connect(db_file) as conn:
    try:
        conn.execute(schema)
        conn.execute('insert into avto(name1,car1,watchmen1,arrivaLog1,departureLog1) values(?,?,?,?,?)', dataforms)
    except sqlite3.OperationalError:
        pass
        conn.execute('insert into avto(name1,car1,watchmen1,arrivaLog1,departureLog1) values(?,?,?,?,?)', dataforms)
