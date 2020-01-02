import sqlite3

connector = sqlite3.connect("task.db")
cursor = connector.cursor()


def connect():
    cursor.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, title TEXT, dates DATE, description TEXT, location TEXT)")
    connector.commit()


def view():
    cursor.execute("SELECT * FROM task")
    rows = cursor.fetchall()
    return rows


def insert(title, dates, description, location):
    cursor.execute("INSERT INTO task VALUES (NULL,?,?,?,?)", (title, dates, description, location))
    connector.commit()


def search(title='', dates='', description='', location=''):
    cursor.execute("SELECT * FROM task WHERE title=? or dates=? or description=? or location=?", (title, dates, description, location))
    result = cursor.fetchall()
    return result


def delete(tid):
    cursor.execute("DELETE FROM task WHERE id=?", (tid,))
    connector.commit()


def update(title, dates, description, location, tid):
    cursor.execute("UPDATE task SET title=?, dates=?, description=?, location=? WHERE id=?", (title, dates, description, location, tid))
    connector.commit()


def drop():
    cursor.execute("DROP TABLE IF EXISTS task")


connect()
print(view())
