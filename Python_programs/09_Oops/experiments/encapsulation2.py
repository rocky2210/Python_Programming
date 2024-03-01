class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder    # Public attribute
        self.__balance = balance    # Private attribute
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    
    def get_balance(self):
        return self.__balance   # Getter method
    
    def set_balance(self, balance):
        if balance >=0:
            self.__balance = balance    # Setter method

# Create a bank account
account = BankAccount("Rocky", 1000)

# Access and modify the public attribute directly
print(f"Account holder: {account.account_holder}")

# Access and modify the private attribute using methods
account.deposit(500)  # Output: Deposited $500. New balance: $1500
account.withdraw(200)  # Output: Withdrew $200. New balance: $1300

# Try to access the private attribute directly (this will not work)
# print(account.__balance)  # This will raise an AttributeError

# Access the private attribute using the getter method
print(f"Current balance: ${account.get_balance()}")  # Output: Current balance: $1300

# Modify the private attribute using the setter method
account.set_balance(2000)
print(f"Updated balance: ${account.get_balance()}")  # Output: Updated balance: $2000

"""
    Output:
        Account holder: Rocky
        Deposited $500. New balance: $1500
        Withdrew $200. New balance: $1300
        Current balance: $1300
        Updated balance: $2000
"""