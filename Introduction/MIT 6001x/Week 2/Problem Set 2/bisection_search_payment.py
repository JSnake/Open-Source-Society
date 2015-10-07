balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
uppperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
newBalance = balance

while abs(newBalance) > 0.01:
    newBalance = balance
    monthlyPayment = lowerBound + (uppperBound - lowerBound) / 2
    for i in xrange(0, 12):
        newBalance -= monthlyPayment
        newBalance += monthlyInterestRate * newBalance
    if newBalance < 0:
        uppperBound = monthlyPayment
    else:
        lowerBound = monthlyPayment

print "Lowest Payment:", round(monthlyPayment, 2)