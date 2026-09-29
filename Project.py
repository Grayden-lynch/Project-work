#Holds users and their passwords
users = {"Grayden":"Pass1",
         "Isaiah":"Pass2",
         "Gus":"Pass3"}

login = input("Enter your name: ")

#Nested selection statement
if login in users:
  password = input("Enter password:")

  #Loop until password is correct

  while password != users[login]:
    print("Incorrect Password, Try again.")
    password = input("Enter password:")

  if password == users[login]:
      print("Login Successful!")
  
else:
  print("Unknown User.")
  exit()

print(f"Hello {login} welcome to SpendSmart")

#Calculating final balance after expenses are entered
paycheck = float(input("Enter paycheck amount:"))
balance = paycheck
expense = float(input("Enter expense(0 to stop):"))

while expense != 0:
  balance = balance - expense
  expense = float(input("Enter expense(0 to stop):"))
print(f"Your final balance is {balance}.")







