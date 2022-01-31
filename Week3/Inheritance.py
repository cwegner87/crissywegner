class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

class BankUser1(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)


class BankUser2(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 100

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)

class BankUser3(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 200

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)

Testuser1 = BankUser1("Sally", "bankuser1@gmail.com", "user1password")
Testuser2 = BankUser2("Ben", "bankuser2@gmail.com", "user2password")
Testuser3 = BankUser3("Lacy", "bankuser3@gmail.com", "user3password")    

Testuser1.check_balance()
Testuser2.check_balance()
Testuser3.check_balance()