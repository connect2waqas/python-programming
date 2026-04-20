class Bank:
    def __init__(self,balance,HBL,acc_no,name):
        self.bank_balance = balance
        self.HBL_number = HBL
        self.acc_no = acc_no
        self.customer_name = name
    

    def deposit(self,amount):
        self.bank_balance += amount
        print(f"The New balance is: {self.bank_balance}")

b1 = Bank(2000,"Hbl Timergara",18300,"Waqas")

# print(f"The bank balance is: {b1.bank_balance}")
# amount = int(input("enter your deposit amount: "))

# b1.bank_balance = b1.bank_balance + 1000
# print(b1.bank_balance)

# __dict__ Method:

print(b1.__dict__)

# __new__

