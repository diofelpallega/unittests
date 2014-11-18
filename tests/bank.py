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

    def withdraw_ammount(self, account_number, ammount):
        wait_value =  self.accounts.get(account_number) 
        new_value = wait_value - ammount
        return new_value
