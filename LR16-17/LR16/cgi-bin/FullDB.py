import sqlite3
con = sqlite3.connect('database.db')
def sql_fetch(con):
    cursorObj = con.cursor()
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
print("<h1>Все записи в базе данных</h1>")
print(sql_fetch(con))
print("""</body>
</html>""")