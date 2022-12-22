import cgi
import sqlite3
con = sqlite3.connect('database.db')
form = cgi.FieldStorage()
car = form.getfirst("in_car", "не задано")
cursorObj = con.cursor()
cursorObj.execute('''UPDATE avto
                    SET car1='Ford Mustang';''')

def sql_fetch(con):

    cursorObj.execute('SELECT * FROM avto')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
</head>
<body>""")
print("<h1>заменить все названия автомобилей на Ford Mustang </h1>")
print(sql_fetch(con))
print("""</body>
</html>""")