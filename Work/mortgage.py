# mortgage.py
#
# Exercise 1.7
"""Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage,
Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly
payment is $2684.11"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month += 1
    principal = principal * (1 + rate / 12) - payment
    total_paid += payment

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)
