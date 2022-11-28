import CC

running = True

while running == True:

    name = input('Which Credit Card are you calculating?')
    balance = input('\nHow much do you currently owe?')
    float(balance)
    interest = input('\nWhat is the interest rate for this Credit Card?')
    float(interest)
    minpayment = input('\nWhat is the minimum monthly payment amount?')                 
    float(minpayment)
    if input('\nDo you want to make payments higher than the minimum?') == 'y':
        proppayment = input('\nHow much do you want to pay each month?')
    else:
        proppayment = minpayment
    float(proppayment)

    name = CC.CreditCard('name', balance, interest, minpayment, proppayment)
    
    name.payoffcalc()
    
    input('\nPress any key to continue... ')
    
    if input('\nWould you like to do calculations for another Credit Card?') == 'n':
        running = False
  