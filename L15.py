import sqlite3

con = sqlite3.connect('workshop.db')
cursorObj = con.cursor()


def fk_on():
    cursorObj = con.cursor()
    cursorObj.execute("PRAGMA foreign_keys = ON")
    con.commit()
fk_on()


def create():
    cursorObj.execute("CREATE TABLE IF NOT EXISTS executor(id INT primary key, name TEXT)")
    con.commit()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS task(id INT primary key, name TEXT, price INT)")
    con.commit()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS customer(id INT primary key, name TEXT)")
    con.commit()

    cursorObj.execute(
        "create table if not exists orders(id INT primary key," + \
        "executorId INT, customerId INT, taskName TEXT)")
    con.commit()


create()


def drop_table():
    cursorObj = con.cursor()
    cursorObj.execute("drop table if exists orders")
    con.commit()

tasks = [(0, 'Cleaning', 1000),
         (1, 'Deep Cleaning', 1300),
         (2, 'Replacement Parts', 1200),
         (3, 'Deep Replacement Parts', 1500),
         (4, 'Full Package', 2500)]

customers = [(0, 'Bogdan'),
             (1, 'Dogdan'),
             (2, 'Logdan'),
             (3, 'Zogdan'),
             (4, 'Wogdan'),
             (5, 'Sanya')]

executors = [(0, 'Papich'),
             (1, 'Lapich'),
             (2, 'Zapich'),
             (3, 'Kapich')]

orders = [(0, 1, 3, 'Cleaning'),
          (1, 1, 4, 'Deep Cleaning'),
          (2, 2, 5, 'Cleaning'),
          (3, 3, 1, 'Full Package'),
          (4, 0, 3, 'Replacement Parts'),
          (5, 3, 0, 'Replacement Parts'),
          (6, 2, 2, 'Full Package'),
          (7, 0, 1, 'Deep Replacement Parts'),
          (8, 1, 2, 'Deep Replacement Parts'),
          (9, 0, 2, 'Cleaning')]

def sql_insert():
    cursorObj = con.cursor()
    cursorObj.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)
    con.commit()

def delete_from_executor():
    cursorObj = con.cursor()
    cursorObj.execute("delete from executor where id=(0)")
    con.commit()

def delete_from_task():
    cursorObj = con.cursor()
    cursorObj.execute("delete from task where name=('Чистка 1 бабиджона')")
    con.commit()

def select():
    cursorObj = con.cursor()
    cursorObj.execute("select id, name from task where price>1300")
    for i in cursorObj.fetchall():
        print(i)
    print("\n")
    cursorObj.execute("select id, name from executor where name = 'Papich' or name = 'Lapich'")
    for i in cursorObj.fetchall():
        print(i)
    print("\n")
    cursorObj.execute("select * from customer")
    for i in cursorObj.fetchall():
        print(i)
    print("\n")
    cursorObj.execute("select taskName from orders where executorId = 2")
    for i in cursorObj.fetchall():
        print(i)
    con.commit()

def update():
    cursorObj = con.cursor()
    cursorObj.execute('update task set price = 1000 where name = "Cleaning"')
    cursorObj.execute('update executor set name = "WWWW" where name = "Papich"')
    cursorObj.execute('update customer set name = "WWWW" where name = "Bogdan" or name = "Sanya"')
    con.commit()

def delete():
    cursorObj = con.cursor()
    cursorObj.execute('delete from task where name = "Full Package"')
    cursorObj.execute('delete from orders where customerId = 1')
    cursorObj.execute('delete from executors')
    con.commit()

con.close()
