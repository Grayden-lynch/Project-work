users = {"Grayden":"Pass1",
         "Isaiah":"Pass2",
         "Gus":"Pass3"}

expenses_list = ["Housing", "Food", "Transportation", "Debt payments", "Savings", "Other"]


class Budget:
    def __init__(self, paycheck):
        self.paycheck = paycheck
        self.balance = paycheck
        self.budget_info = ("SpendSmart", "Monthly Budget", "USD")

    def add_expense(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Your final balance is {self.balance}")
        print("Budget information:", self.budget_info)



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
balance = Budget(paycheck)

file = open("expenses.txt", "w")

file.write("Category,Expense\n")

for expenses in expenses_list:
    expense = float(input(f"{expenses} cost: "))

    if expense < 0:
        print("You typed in a negative expense. Try again.")
        expense = float(input(f"{expenses} cost: "))

    balance.add_expense(expense)

    # Write expense to file
    file.write(f"{expenses},{expense}\n")


file.close()

balance.display_balance()








