# https://inloop.github.io/sqlite-viewer/
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('SELECT * from ips ORDER BY asn')

columns = [item[0] for item in cur.description]
print(f'{columns=}')

# tuple of tuples
print(f'{cur.description=}')

# flatten to tuples by unpacking - each tuple becomes an argument
print(f'{[*cur.description]=}')

# aggregates the tuples, the first gets all the column names
names, *_ = list(zip(*cur.description))
print(f'{names=}')

# returns an iterator to a list of tuples
rows = cur.fetchall()

# insert row names on top
rows.insert(0, names)
print(f'{rows=}')

# unpack index and fields from tuple
for n, (ip, domain, asn) in enumerate(rows):
    # print(n, ip, domain, asn)
    # print('{n:02d} | {ip:15s} | {domain:20s} | {asn:3s}'.format(n=n, ip=ip, domain=domain, asn=asn))
    # print('{0:02d} | {1:15s} | {2:20s} | {3:3s}'.format(n, ip, domain, asn))
    # print('{:02d} | {:15s} | {:20s} | {:3s}'.format(n, ip, domain, asn))
    print('%02d | %15s | %20s | %3s' % (n, ip, domain, asn))

con.close()
