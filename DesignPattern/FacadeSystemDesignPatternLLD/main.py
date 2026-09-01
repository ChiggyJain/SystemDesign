
class Account:
    
    def __init__(self):
        pass

    def verifyAccount(self, account_number: str):
        print(f"Account verified: {account_number}")
        return True

class Security:

    def __init__(self):
        pass

    def checkPin(self, pin: int):
        print(f"Pin verified")
        return True

class Funds:

    def __init__(self):
        pass

    def hasSufficientFunds(self, amount: float):
        print(f"Sufficient funds available")
        return True
    
    def debit(self, amount):
        print(f"Debited: {amount}")
        return True

class BankFacade:

    def __init__(self):
        self.account_class_obj = Account()
        self.security_class_obj = Security()
        self.funds_class_obj = Funds()

    def withdraw(self, account_number: str, pin: int, amount: float):
        print(f"Starting withdrawal process")
        if self.account_class_obj.verifyAccount(account_number) and self.security_class_obj.checkPin(pin) and self.funds_class_obj.hasSufficientFunds(amount):
            self.funds_class_obj.debit(amount)
            print(f"Finished and succeed withdrawal process")
        else:
            print(f"Withdrawal failed")


def Demo():
    
    bank_facade_class_obj = BankFacade()
    bank_facade_class_obj.withdraw("ABC1", 123, 10)


Demo()

