
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class StripePaymentAdapter(PaymentProcessor):

    def __init__(self, card_number):
        self.card_number = card_number
        # stripe payment gateway client object with credentials
        # self.client = StripePaymentGateway()

    def pay(self, amount: float):
        # self.client.makePayment(self.card_number, amount)
        print(f"Stripe: Paid {amount}")


class RazorPayPaymentAdapter(PaymentProcessor):

    def __init__(self, phone_number):
        self.phone_number = phone_number
        # razor pay payment gateway client object with credentials
        # self.client = RazorPayPaymentGateway()

    def pay(self, amount: float):
        # self.client.createPayment(self.phone_number, amount)
        print(f"Razorpay: Paid {amount}")
    

def Demo():
    
    selected_payment_adapter = None

    print(f"Select Payment Gateway")
    print(f"1. Stripe")
    print(f"2. Razorpay")
    
    enter_choice_number = int(input("Enter your choice number: "))
    match (enter_choice_number):
        case 1:
            selected_payment_adapter = StripePaymentAdapter("ABCBC122")
        case 2:
            selected_payment_adapter = RazorPayPaymentAdapter("122333")
    
    if selected_payment_adapter!=None:
        selected_payment_adapter.pay(100)
        


Demo()