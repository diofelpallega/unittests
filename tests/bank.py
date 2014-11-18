class Bank(object):
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        if type(account.account_number) == str:            
            self.accounts[account.account_number] = account.balance
        else: 
            print "Invalid Account"

    def get_account_balance(self, account_number):
        if type(account_number) == str:
            return self.accounts.get(account_number)
        else:
            print "Invalid account number"

    def withdraw_amount(self, account_number, amount):
        if type(account_number) == str and type(amount) == int and int(self.accounts.get(account_number)) > amount:
            wait_value =  self.accounts.get(account_number) 
            new_value = wait_value - amount
            return new_value
        else: 
            print "error input"
