#Holds users and their passwords
users = {"Grayden":"Pass1",
         "Isaiah":"Pass2",
         "Gus":"Pass3"}

def login_system(users):
  login = input("Enter your name: ")
  while login not in users:
    login = input("Enter your name: ")
  if login in users:
    password = input("Enter password: ")
    #Loop until password is correct       
    while password != users[login]:
      print("Incorrect Password, Try Again.")
      password = input("Enter password: ")
    print("Login Sucessful!")
    return login
  else:
    print("User Unknown.")
#Calls the function
login = login_system(users)

print(f"Hello {login} welcome to SpendSmart")

paycheck = float(input("Enter paycheck amount:"))
balance = paycheck
expense = float(input("Enter expense(0 to stop):"))

while expense != 0:
  if expense < 0:
    print("You typed in a negative expense try again")
    expense = float(input("Enter expense(0 to stop):"))
  balance = balance - expense
  expense = float(input("Enter expense(0 to stop):"))
saving = input("Would you like to save any money?(Y/N)")
if saving == "Y":
  yes = float(input("How much would you like to put in savings?"))
  balance = balance - yes
else:
  print(f"Your final balance is {balance}.")
print(f"Your final balance is {balance}.")








