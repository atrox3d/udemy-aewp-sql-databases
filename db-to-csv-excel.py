import sqlite3
import pandas


con = sqlite3.connect('database.db')
cur = con.cursor()

df = pandas.read_sql(
    'SELECT * FROM ips ORDER BY asn',
    con
)

print(df)

df.to_excel('database.xlsx', index=False)

