login = input("Enter your name: ")
print(f"Hello {login} welcome to SpendSmart")

paycheck = float(input("Enter paycheck amount:"))
balance = paycheck
expense = float(input("Enter expense(0 to stop):"))

while expense != 0:
  balance = balance - expense
  expense = float(input("Enter expense(0 to stop):"))
print(f"Your final balance is {balance}.")

print("hello")




