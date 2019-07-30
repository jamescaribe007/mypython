#!/usr/local/bin/python3.7

def assignAccount():
    try:
      fromFile = open("accounts.csv","r")
      content = fromFile.readlines()
      last_line = content[-1]
      aux = last_line.split(":",1)
      num = int(aux[0]) + 2
      account_number = str(num)
      return account_number
    except FileNotFoundError:
       return "2019000001"


def create():
    print("Client details")
    number = assignAccount()
    name = input("Fist name: ")
    lname = input("Last name: ")
    mail = input("E-Mail: ")
    tel = input("Tel. number: ")
    details = {"number":number, "name":name, "lname":lname, "mail":mail, "tel":tel}
    save(details)
def save(details):
    line = ""
    for item in details:
        if line == "":
           line = line+details[item]
        else:
           line = line+":"+details[item]
    toFile = open("accounts.csv","a+")
    toFile.write(line+"\n")
    toFile.close()
    print("New account has been created")

def display():
    fromFile = open("accounts.csv", "r")
    content = fromFile.readlines()
    for record in content:
        print(record, end ="")
        
def menu():
    print("Bank Interntional System")
    print("------------------------")
    print("1. Create account")
    print("2. List accounts")
    print("5. Exit ")

#-----------------------------------------------------

execute = True

while execute == True:
  menu()
  option = input("Chose option: ")
  if option == '1':
     create()
  elif option == '2':
     display()
     #print(assignAccount())
  elif option == '5' or option == 'exit':
       execute = False
  else:
     print("You have to select one of above options")

    for item in details:
        if line == "":
           line = line+details[item]
        else:
           line = line+":"+details[item]
    toFile = open("accounts.csv","a+")
    toFile.write(line+"\n")
    toFile.close()
    print("New account has been created")
    

    
