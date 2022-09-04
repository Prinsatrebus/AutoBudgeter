import time

class CreditCard:
    def __init__(self, name, balance, interest, minpayment, proppayment):
        self.name = name
        self.balance = float(balance)
        self.interest = float(interest)
        self.minpayment = float(minpayment)
        self.proppayment = float(proppayment)
        
    def payoffcalc(self):
        
        payment = self.proppayment
        rembal = self.balance
        payoffamt = float(0)
        payofftime = int(0)
    
        while rembal > 0:
            payofftime += 1
            rembal = (rembal+(rembal*self.interest)/12)
            rembal -= payment 
            payoffamt += payment
            
        print('\nThis credit card will take {0} months to pay off with a total balance of ${1} having been paid at the current rate'.format(payofftime, payoffamt))
        
        time.sleep(1)
        
        payment += 20
        rembal = self.balance
        payoffamt = float(0)
        payofftime = int(0)
        
        while rembal > 0:
            payofftime += 1
            rembal = (rembal+(rembal*self.interest)/12)
            rembal -= payment 
            payoffamt += payment
        
        print('\nIf you make payments of $20 more than the minimum, then this credit card will take {0} months to pay off with a total balance of ${1} having been paid at the current rate'.format(payofftime, payoffamt))
        
        time.sleep(1)
        
        payment = self.proppayment * 2
        rembal = self.balance
        payoffamt = float(0)
        payofftime = int(0)
        
        while rembal > 0:
            payofftime += 1
            rembal = (rembal+(rembal*self.interest)/12)
            rembal -= payment 
            payoffamt += payment
        
        print('\nIf you make double payments, then this credit card will take {0} months to pay off with a total balance of ${1} having been paid at the current rate'.format(payofftime, payoffamt))