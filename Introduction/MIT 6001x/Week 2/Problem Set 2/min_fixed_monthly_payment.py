balance = 3329
annualInterestRate = 0.2
newBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 0

while newBalance > 0:
    month = 1
    monthlyPayment += 10
    newBalance = balance
    while newBalance > 0 and month <= 12:
        newBalance -= monthlyPayment
        interest = monthlyInterestRate * newBalance
        newBalance += interest
        month += 1

print "Lowest Payment:", monthlyPayment