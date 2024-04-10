import sqlite3
#connection = sqlite3.connect('storage.sqlite')
#cursor = connection.cursor()

#Data = [("Mike","blue"),("John","red")]

#cursor.executemany(f"INSERT INTO data VALUES (?,?)", Data)

#connection.commit()
##connection.execute('''CREATE TABLE IF NOT EXISTS data (first_name TEXT, last_name TEXT)''')



#cursor.close()
#connection.close()

connction = sqlite3.connect("banking_system")

cursor = connction.cursor()

command_1 = """CREATE TABLE IF NOT EXISTS banking_system(balence INTEGER,acount_number INTEGER PRIMARY KEY, acount_holder TEXT)"""

cursor.execute(command_1)

cursor.execute("INSERT INTO banking_system VALUES (100,1,'Mike')")
cursor.execute("INSERT INTO banking_system VALUES (100,2,'Jake')")
cursor.execute("INSERT INTO banking_system VALUES (100,3,'Adam')")

cursor.execute("SELECT * FROM banking_system")
results =cursor.fetchall()
print(results)

cursor.execute("UPDATE banking_system SET balence = balence + 100 WHERE acount_number = 1")
cursor.execute("SELECT * FROM banking_system")
new_results = cursor.fetchall()
print(new_results)