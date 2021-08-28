from abc import ABC, abstractmethod
class pizza(ABC):
    def payBill(self, amount):
        print("Your purchase amount: ",amount)
    #this function tells us to pass argument, no indication how or what
        #type of data it will be.
        @abstractmethod
        def payment(self, amount):
            pass

class DebitCardPayment(pizza):
    #this is defined how to implement the payment function from its parent payBill class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $10.00 limit '.format(amount))

obj = DebitCardPayment()
obj.payBill("$15.00")
obj.payment("$15.00")
