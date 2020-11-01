# Sean Mayers
# 11/1/2020
# CheckingAccount 

""" Your assignment this week you will build a CheckingAccount class
    and associated driver application.  The class should contain
    appropriate attributes that you would find in a normal checking account:
    name, address, accounts number, balance, etc
 
   The balance should be "private" to the class since it should only be changed
   through appropriate debit/credit methods.  Recall, you can simulate
   the private aspect using the _ character at the start of the variable name. 
  
   The class should be saved in a file called CheckingAccount.py """

# Class created
class CheckingAccount:
    # develop constructor; function decalared inside of class
    def __init__(self, name, address, account_number, balance):
        #attributes / intance variables
        self.__name = name
        self.__address = address
        self.__accountNumber = account_number
        self.__balance = balance
                 
    # function to credit account
    def creditAccount(self, amount):
        self.__balance = self.__balance + amount
                  
    # function to debit account
    def debitAccount(self, amount):
        if self.__balance < amount:
            print("Account balance ${:.2f} is low.  \nThe amount of ${:.2f} exceeds the allowable deduction and will not be completed.".format(self.__balance, amount))
                
        else:
            self.__balance = self.__balance - amount
                 
    # function for displaying balance
    def displayBalance(self):
        print("\nAccount Number: {} \nAccount Holder Name: {} \nAccount Balance: ${:.2f}".format(self.__accountNumber, self.__name, self.__balance))
                 
               
    
    
    