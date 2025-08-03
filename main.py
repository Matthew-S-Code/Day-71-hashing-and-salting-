from replit import db
import random, os, time

def addUser():
  time.sleep(1)
  os.system("clear")
  user = input("Enter a username\n>").strip()
  password = input("Enter a password\n>").strip()
  keys = db.keys()
  if user in keys:
    print("Username already in use")
    return
  salt = random.randint(1000,9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  db[user] = {"password": newPassword, "salt": salt}
  print("User Added\n")
  time.sleep(1)
  os.system("clear")

def login():
  time.sleep(1)
  os.system("clear")
  user = input("Enter a username\n>").strip()
  password = input("Enter a password\n>").strip()
  keys = db.keys()
  if user not in keys:
    print("Username does not exist")
    return
  salt = db[user]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  if db[user]["password"]==newPassword:
    print("Logged in")
    time.sleep(1)
    os.system("clear")
  else:
    print("Invalid username or password")


while True:
  menu = input("Add user = '1' or Login = '2'\n>")
  if menu == "1":
    addUser()
  elif menu == "2":
    login()
  else:
    keys = db.keys() # this is just to check that it was working, the else should just be invalid input
    for key in keys:
      print(db[key])
