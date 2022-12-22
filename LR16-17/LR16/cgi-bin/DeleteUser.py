import cgi
import sqlite3
con = sqlite3.connect('database.db')
form = cgi.FieldStorage()
arrivaLog = form.getfirst("in_arrivaLog", "не задано")
cursorObj = con.cursor()
cursorObj.execute('''DELETE FROM avto 
                    WHERE arrivaLog1='12.02.2024';''')
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
print("<h1>Удаление записи дата прибытия =12.02.2024 </h1>")
print(sql_fetch(con))
print("""</body>
</html>""")