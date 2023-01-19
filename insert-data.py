import sqlite3

cur = sqlite3.connect('database.db').cursor()

new_rows = [
    ('100.100.100.100', 'a.b.c', 100),
    ('200.200.200.200', 'd.e.f', 200),
]

cur.executemany(
    'INSERT into ips VALUES(?, ?, ?)',
    new_rows
)
cur.connection.commit()

cur.execute(
    'SELECT * from ips'
)

print(cur.fetchall())
