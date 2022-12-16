import cgi

form = cgi.FieldStorage()
text=form.getfirst("TEXT", "")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT: {}</p>".format(text))
print("""</body>
        </html>""")