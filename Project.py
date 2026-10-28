#Holds users and their passwords
users = {"Grayden":"Pass1",
         "Isaiah":"Pass2",
         "Gus":"Pass3"}

expenses_list = ["Housing", "Food", "Transportation", "Debt payments", "Savings", "Other"]



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

for expenses in expenses_list:
  expense = float(input(f"{expenses} cost:"))
  if expense < 0:
    print("You typed in a negative expense try again")
    expense = float(input(f"Enter "))
  balance = balance - expense

print(f"Your final balance is {balance}.")








