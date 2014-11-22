
class Account(object):
    def __init__(self, account_number, balance):
        if type(account_number) == str and type(balance) == int:
            self.account_number = account_number
            self.balance = balance
        else:
            print "error inputs"
 
class AccountWithdraw(object):
    def __init__(self, account_number, balance, withdraw_amount):
        if  type(account_number) == str and type(balance) == int and type(withdraw_amount) == int and balance > withdraw_amount: 
            self.balance = balance - withdraw_amount
        else:
            print "invalid inputs"
     
