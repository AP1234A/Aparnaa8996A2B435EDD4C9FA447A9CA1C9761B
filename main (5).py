# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Back_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount      Deposited: ", amount)

    def withdraw(self):
      amount = float(input("Enter amount to be Withdrawn: "))
      if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdraw: ", amount)
      else:
          print("\n Insufficient balance  ")
          
    def display(self):
        print("\n Net Available Balance=", self.balance)

# Driver code

# creating an object of class
s = Back_Account()

# calling function with that class object
s.deposit()
s.withdraw()
s.display()
