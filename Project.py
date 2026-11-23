#users and their passwords
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

def budget_status(paycheck, remaining_balance):
    total_expenses = paycheck - remaining_balance
    print(f"Total expenses: ${total_expenses:,.2f}")

    if remaining_balance < 0:
        print(f"You are over budget by ${abs(remaining_balance):,.2f}.")
    elif remaining_balance == 0:
        print("You have used your entire paycheck.")
    else:
        print(f"You are within budget with ${remaining_balance:,.2f} left.")

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

def get_paycheck():
   paycheck = float(input("Enter Paycheck Amount: "))
   return paycheck
paycheck = get_paycheck()
balance = Budget(paycheck)

file = open("expenses.csv", "w")

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
budget_status(paycheck, balance.balance)











