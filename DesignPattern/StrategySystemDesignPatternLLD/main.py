
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditcardPaymentStrategy(PaymentStrategy):

    def __init__(self, name: str, card_number: str, cv_number: str):
        self.name = name
        self.card_number = card_number
        self.cv_number = cv_number
    
    def pay(self, amount: float):
        print(f"Processing {amount} payment with credit card belonging to {self.name}")

class GooglePayPaymentStrategy(PaymentStrategy):

    def __init__(self, pin: str):
        self.pin = pin
    
    def pay(self, amount: float):
        print(f"Processing {amount} payment with google-pay")

class PaymentProcessor:
    
    def __init__(self):
        self.payment_strategy_class_obj = None

    def setPaymentStrategy(self, payment_strategy_class_obj):
        self.payment_strategy_class_obj = payment_strategy_class_obj

    def processPayment(self, amount: float):
        self.payment_strategy_class_obj.pay(amount)


def Demo():
    
    selected_payment_strategy_class_obj = None
    
    print(f"Select Payment Method: ")
    print(f"1. Creditcard")
    print(f"2. GooglePay")

    entered_choice_number = int(input(f"Enter your choice number: "))
    match(entered_choice_number):
        case 1:
            entered_name = str(input("Enter your name: "))
            entered_card_number = str(input("Enter your card number: "))
            entered_card_cv_number = str(input("Enter your card cv number: "))
            selected_payment_strategy_class_obj = CreditcardPaymentStrategy(entered_name, entered_card_number, entered_card_cv_number)
        case 2:
            entered_pin = str(input("Enter your google pay pin: "))
            selected_payment_strategy_class_obj = GooglePayPaymentStrategy(entered_pin)

    if selected_payment_strategy_class_obj!=None:
        amount = 100
        payment_processor_class_obj = PaymentProcessor()
        payment_processor_class_obj.setPaymentStrategy(selected_payment_strategy_class_obj)
        payment_processor_class_obj.processPayment(amount)


Demo()
