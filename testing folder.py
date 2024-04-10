import sqlite3

connection = sqlite3.connect('newtorage.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXIST data
(Abdoul)''')

conn.commit()

cur.close()
conn.close()