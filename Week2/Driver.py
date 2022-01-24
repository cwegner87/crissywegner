import CheckingAccount

# asking the user for account details
name = input('Enter account holder name: ')
address = input('Enter  address: ')
accNumber = 'AC123009'
balance = float(input('Enter initial deposit: '))

# new account
newAccount = CheckingAccount.CheckingAccount(name, address, accNumber, balance)


option = ''

# repeat until user type 3 to exit
while option != '3':
    # display options
    print()
    print('Banking Options:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Exit')
    option = input('Enter option: ')

    # credit
    if option == '1':
        amount = float(input('Amount: '))
        newAccount.credit(amount)
        newAccount.displayDetails()
        
    #  debit
    elif option == '2':
        amount = float(input('Amount: '))
        newAccount.debit(amount)
        newAccount.displayDetails()