class CheckingAccount:
    def __init__(self, name, address, accountNumber, balance):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber 
        self._balance = balance

    
    def debit(self, amount):
        
        if(self._balance >= amount):
            self._balance -= amount
        else:
            
            print('BALANCE IS NOT SUFFICIENT!')
    
    # for credit
    def credit(self, amount):
        self._balance += amount

    # account details
    def displayDetails(self):
        print()
        print('ACCOUNT DETAILS')
        print("-"*50); 
        print("ACC NUMBER: ", self.accountNumber)
        print("NAME: ", self.name)
        print("ADDRESS: ", self.address)
        print("BALANCE: ", self._balance, "$")
        print("-"*50); 
        print()