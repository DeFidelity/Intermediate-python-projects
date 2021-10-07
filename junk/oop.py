# class Customer:
#     def __init__(self, name, membership_trial):
#         self.name = name
#         self.membership_trial= membership_trial

# c1 = Customer("haki" , "gold")
# c2 = Customer("fideh", "diadem")
# print(c1.name, c1.membership_trial)
# print(c2.name, c2.membership_trial)

# class Customer:
#     def __init__(self, name, membership_trial):
#         self.name = name
#         self.membership_trial= membership_trial

# c = [ Customer("haki" , "gold"),
#       Customer("fideh", "diadem")]
# print(c[0].name)

#we can as well define a function in our class inside the innit function
#inheritance
class user:
    def log(self):
        print(self)
class Customer(user):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
# inheritor

    @property
    def name(self):
        print("getting name")
        return self._name
    @name.setter
    def name(self, name):
        print("setting name")
        self._name =name

    @name.deleter
    def name(self):
        del self._name
    def upgrade_customer(self, new_customer):
        self.membership_type = new_customer
    def __str__(self):
        return self.name + " " + self.membership_type
    def print_all_customer(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    __hash__ = None

    __repr__ = __str__
    

c = [ Customer("haki" , "gold"),
      Customer("fideh", "diadem")]
c[0].log
# del c[1].name
print(c)


# print(c[1].membership_type)
# Customer.print_all_customer(c)
# c[1].upgrade_customer("gold")
# print(c)



#  another method is the __str__() method
# it is used to convert anything in the class to a str there by making it possible to print anything

# there are more to adding function to a class and its called custom functionality
#     invoke api
#     update a database
#     charge customer
#     conqure th world 
#     prety anything else
# there is anothe method called __eq__(self, other) it s used to compare anything to anythingif they are equal
