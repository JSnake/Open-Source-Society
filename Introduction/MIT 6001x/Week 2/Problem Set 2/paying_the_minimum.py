def minimum_payment(balance, annual_interest_rate, monthly_payment_rate):
    total_paid = 0
    month = 1

    while month <= 12:
        minimum_payment = monthly_payment_rate * balance
        balance -= minimum_payment
        balance += (annual_interest_rate / 12.0) * balance

        print "Month:", month
        print "Minimum monthly payment:", round(minimum_payment, 2)
        print "Remaining balance:", round(balance, 2)

        total_paid += minimum_payment
        month += 1

    print "Total paid:", round(total_paid, 2)
    print "Remaining balance:", round(balance, 2)

minimum_payment(4213, 0.2, 0.04)
minimum_payment(4842, 0.2, 0.04)
