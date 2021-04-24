class Budget:

    def __init__(self, category):

        self.category = category
        self.amount = 1000

    # methods
    def deposit(self,amount):

        self.amount += amount
        "This is a deposit method"
        return self.amount

    def check_balance(self,amount):
        if self.amount < amount:
            return False
        else:
            return True

    def withdraw(self,amount):
        self.amount -= amount
        return self.amount

    def transfer(self,amount,category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return "You have transferred () to ()".format(amount,category.category)
        else:
            return "you do not have enough balance to perform this transfer"
        pass


category = Budget("Clothing")
print("This is deposits for clothing", category.deposit(500))
print("This is deposit for clothing ", category.withdraw(700))

category_1 = Budget("Food")
print("This is deposit for clothing",category_1.deposit(800))

transfer = category.transfer(500, "Entertainment")
#print(category = budget("clothing"))
#category_1 = budget("Food")
#catogory_2 = budget("Entertainment")
