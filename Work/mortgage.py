# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
overpay = 0

while principal > 0:
    month += 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    print(month, " ", total_paid, " ", principal)

if principal<0:
     overpay = abs(principal)
     total_paid += overpay

print("Total paid: ", round(total_paid, 2))
print("Months", month)
print("Refund: ", overpay)
