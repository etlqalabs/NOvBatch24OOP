class BankAccount:
    def __init__(self,owner,balance,pin):
        self.owner = owner
        self._balance = balance  # protected variable
        self.__pin = pin  # private variable

    def print_public_owner_Name(self):
        print(f"The owner of the bank account is {self.owner} ")

    def print_protected_balance(self):
        print(f"The Balance in the bank account is {self._balance} ")

    def print_private_pin(self):
        print(f"The Pin of the bank account is {self.__pin} ")


class SavingsAcount(BankAccount):
    def __init__(self,owner,balance,pin,interest_rate):
        super().__init__(owner,balance,pin)
        self.interest_rate = interest_rate

    def print_interest_rate(self):
        print(f"Intereest rate is : {self.interest_rate}")

# Object creation of Child class ( SavingsAcount ) to demonstate the accessibility of
# public,protected and private variable
savingAccount = SavingsAcount("Hetu",10000,12345,12)
# Call all the public methods inheritted from Parent class ( BankAccount)
print("below attributes/variables are accessed using public method ..")
savingAccount.print_public_owner_Name()
savingAccount.print_protected_balance()
savingAccount.print_private_pin()
# Call the public interest method from child class iself
savingAccount.print_interest_rate()

# Now Try to ACCESS all the variables direct from Parent class ( BankAccount) using objects of
# child class ( SavingsAccount )
print("below attributes/variables are accessed directly ..")
print(f"The owner is {savingAccount.owner}")
print(f"Balanace in the account is {savingAccount._balance}")
print(f"Pin of the account is not accessible due to it being a private variable")
 # __pin ( provate variable not accessible here )




