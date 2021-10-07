# Banking system
# parent class: user
#holds details about a user
#has a functon to show user details
#child class: bank
#stores details about the account ballance
#stores details about the amount
#allows for deposit withdrawal and check ballance
#Parent CLass
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("personal details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

# CHild class
class Bank(User):
    def __init__(self,name,age,gender):

        super().__init__(name,age,gender)
        self.ballance = 0
    def deposit(self, amount):
        self.amount = amount
        self.ballance = self.ballance + self.amount
        print("Acount ballance updated, your acount ballance is $", self.ballance)
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.ballance:
            print("Insufficient funds, your available ballance is $", self.ballance)
        else:
            self.ballance = self.ballance - amount
            print("transaction sucessful, your account ballance is $", self.ballance)
    def check_ballance(self):
        self.show_details()
        print("Acount ballance updated, your acount ballance is $", self.ballance)
    
name = input("pls input your name? ")
age = input("what is users age? ")
gender = input("input user gender: ")
deposit_amount = int(input("How much do you want to save? "))
withdraw_amount = int(input("How much do you want to withdraw? "))
    
fideh = User(name,age,gender)
fideh = Bank(name,age,gender)
fideh.deposit(deposit_amount)
fideh.withdraw(withdraw_amount)
fideh.check_ballance()