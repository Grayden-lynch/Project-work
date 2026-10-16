#Holds users and their passwords
users = {"Grayden":"Pass1",
         "Isaiah":"Pass2",
         "Gus":"Pass3"}

def login_system(users):
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
  balance = balance - expense
  expense = float(input("Enter expense(0 to stop):"))
print(f"Your final balance is {balance}.")








