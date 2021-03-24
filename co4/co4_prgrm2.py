class Bank_Account:
    def __init__(self,accno,name,type_of_account,bal):
        self.accno=accno
        self.name=name
        self.type_of_account=type_of_account
        self.bal=bal

    def deposit(self,amount):
        self.bal=self.bal+amount
        print("amount successfully deposited")
        return self.bal
    def withdraw(self,amount):
        if amount>self.bal:
            print("insufficient balance")
            return self.bal
        else:
            self.bal=self.bal-amount
            print("amount successfully withdrawed")
            return self.bal

b=Bank_Account(1001,"ammu","savings",5000)
damount=float(input("enter the amount to be deposited:"))
print("account balance:",b.deposit(damount))
wamount=float(input("enter the amount to be withdraw:"))
print("account balance:",b.withdraw(wamount))