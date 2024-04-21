import sqlite3


connction = sqlite3.connect("banking_system")   #forming a connection with the database

cursor = connction.cursor()     #creating a cursor that will execute my Sqlite3 commands

command_1 = """CREATE TABLE IF NOT EXISTS banking_system(balence INTEGER,acount_number INTEGER PRIMARY KEY, acount_holder TEXT)"""     #creating my database tht will hold my data

cursor.execute(command_1)

#cursor.execute("INSERT INTO banking_system VALUES (100,1,'Mike')")
#cursor.execute("INSERT INTO banking_system VALUES (100,2,'Jake')")
#cursor.execute("INSERT INTO banking_system VALUES (100,3,'Adam')")

#cursor.execute("SELECT * FROM banking_system")
#results =cursor.fetchall()
#print(results)

#cursor.execute("UPDATE banking_system SET balence = balence + 100 WHERE acount_number = 1")
#cursor.execute("SELECT * FROM banking_system")
#new_results = cursor.fetchall()
#print(new_results)


#Above is me learning basic command for SQlite3  like adding deleting,etc

def greeting():
  print("Welcome to the banking system")
def Options():
  print("Here are some of the options")
  print("1.Check your balence")
  print("2.Deposit money")
  print("3.Withdraw money")
  print("4.create/delete acount")
  print("5.Modify acount")
  print("6.Exit")
def check_balence():
  print(cursor.execute(f"SELECT balence FROM banking_system"))
  new_result = cursor.fetchall()
  print(new_result)
def deposit_money():
  deposit = int(input("How much money would you like to deposit "))
  print("What is your acount number")
  acount_number = int(input())
  cursor.execute(f"UPDATE banking_system SET balence = balence + {deposit} WHERE acount_number = {acount_number}")
  cursor.execute("SELECT * FROM banking_system")   #testing
  new_result = cursor.fetchall()
  print(new_result)
def withdraw_money():
  withdraw = int(input("How much money would you like to withdraw "))
  acount_number2 = int(input("What is your acount number "))
  cursor.execute(f"UPDATE banking_system SET balence = balence - {withdraw} WHERE acount_number = {acount_number2}")
  cursor.execute("SELECT * FROM banking_system")
  new_result = cursor.fetchall()
  print(new_result)
def create_delete():
  print("Would you like to create or delete an acount")
  print("1.Create")
  print("2.Delete")
  choice = int(input())
  if choice == 1:
    acount_holder89 = str(input("What is the acount holders name "))
    acount_number3 = int(input("What is the acount number "))
    balence89 = int(input("What is the balence "))
    cursor.execute(f"INSERT INTO banking_system VALUES({balence89},{acount_number3},'{acount_holder89}')")
    cursor.execute("INSERT INTO banking_system VALUES(500,6,'Jamal')")
    cursor.execute("SELECT * FROM banking_system")
    new_result = cursor.fetchall()
    print(new_result)
    print("Your account has been set up and the password is 1234")
  elif choice == 2:
    acount_number4 = int(input("What is the acount number "))
    cursor.execute(f"DELETE FROM banking_system WHERE acount_number = {acount_number4}")
    cursor.execute("SELECT * FROM banking_system")
    new_result = cursor.fetchall()
    print(new_result)
    print("your account has been succesfully deleted") # a function for creating/delteing accounts
def modify():
  print("1.Modify account holder")
  print("2.Modify account number")
  modify = int(input("What would you like to modify"))
  if modify == 1:
    account_number55 = int(input("What is the account number "))
    acount_holder2 = str(input("What do you want the new acount holders name to be "))
    cursor.execute(f"UPDATE banking_system SET acount_holder = {acount_holder2} WHERE acount_number = {acount_number}")
    cursor.execute("SELECT * FROM banking_system")
    new_result = cursor.fetchall()
    print(new_result)
  elif modify == 2:
    account_number56 = int(input("What is the account number "))
    acount_number5 = str(input("What do you want the new acount number to be "))
    cursor.execute(f"UPDATE banking_system SET acount_number = {acount_number5} WHERE acount_number = {account_number56}")
    cursor.execute("SELECT * FROM banking_system")
    new_result = cursor.fetchall()
    print(new_result)   # A function for changing your account
def login():
  first_pass = int(input("What is the account number"))
  Password = str((input("Enter your password: ")))
  if Password == "1234":
    print("Welcome")
  else:
    print("Wrong password please exit and try again")
    exit()     #A univeral pasword that is need before moving on to the banking system
    
###############################

greeting()
login()
Options()               # A list of options I made
for x in range(10):     #How many times my bank program runs
  Q = int(input("Please choose a number"))   #How the user choses what they want to do
  while Q != 1 and Q != 2 and Q != 3 and Q != 4 and Q != 5:
    print("sorry I do not understand")
    Q = int(input("Please choose a number: "))  #Below are the options the user picks
  if Q == 1:
    check_balence()
  elif Q == 2:
    deposit_money()
  elif Q == 3:
    withdraw_money()
  elif Q == 4:
    create_delete()
  elif Q == 5:
    modify()
  elif Q == 6:
    print("I hope I was able to help have a nice day")
    exit()