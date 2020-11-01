# Sean Mayers
# 11/1/2020


# importing the class
from CheckingAccount import CheckingAccount

# object created from CheckingAccount
accountDemo = CheckingAccount("Sean Mayers", "555 Jan Drive", 58230121, 73.5)

# credit and debit transactions
accountDemo.creditAccount(40.00)
accountDemo.debitAccount(125.00)
accountDemo.debitAccount(35.00)  # will be deducted from account if balance is greater
accountDemo.debitAccount(35.00)  # will be deducted from account if balance is greater




# balance of account
accountDemo.displayBalance()

