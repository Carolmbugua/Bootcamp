# class Atm_card:
#     Bank_name ="Welcome to KCB Bank"
#     balance = 0
#
#     def __init__(self,pin,balance,color):
#         self.p = pin
#         self.b = balance
#         self.c = color
#     # def enter_pin(self):
#     #     if self.p == 5666:
#     #         return self.p, "Pin Accepted!"
#     #     else:
#     #         return "Wrong PIN!"
#     def check_balance(self):
#         return self.b
#     def deposit(self,dep):
#           self.d = dep
#           if dep >0:
#               self.b = self.b + self.d
#               return("Balance:",self.b)
#
#
#     def withdraw(self):
#         withdraw = input("Enter amount to withdraw:")
#         if self.check_balance() < int(withdraw) :
#             return("No Sufficient Funds")
#
#         elif self.check_balance()>int(withdraw):
#             self.b = self.b - int(withdraw)
#             return(("Withdrawal Successful!"))
#
#
#
# a1 = Atm_card((input("Enter pin:")),554 ,"Red")
# print(a1.Bank_name)
# print(a1.deposit(34455))
# print(a1.withdraw())
# print(a1.check_balance())

#OR
class Atm_Card:
    name = "Welcome to barclays Bank"
    pin = 0
    balance = 0

    def __init__(self,pin,balance,color):
        self.p = pin
        self.b = balance
        self.c = color

    def set_pin(self):
        pin = 7889
        if self.p != pin:
            return "Wrong PIN!"
        else:
            return "PIN Accepted"

    def check_balance(self):
        return self.b

    def deposit(self,dep):
        self.d = dep
        if dep >0:
            self.b = self.b +self.d
            print(("{} is deposited in your Account".format(self.d)),("Balance:",self.b))

    def withdraw(self,):
        withdraw = input("Enter amount to withdraw:")
        if self.check_balance() < int(withdraw):
            return ("No Sufficient Funds")

        elif self.check_balance() > int(withdraw):
            self.b = self.b - int(withdraw)
            return (("Withdrawal Successful!"),("Balance:",self.b))


a2 = Atm_Card(3444,555,"RED")
print(a2.name)
print(a2.check_balance())
print(a2.deposit(45667))
print(a2.withdraw())