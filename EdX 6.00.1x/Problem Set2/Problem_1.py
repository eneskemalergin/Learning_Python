## Problem Set 2 - Problem 1

'''Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance
, and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0

Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41

instead of

Remaining balance: 813.4141998135 

Finally, print out the total amount paid that year and the remaining balance at the end
of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0

'''

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# I need a loop for 12 months
# after execution of loop is done print() the total
# at the end...
# print("Total paid: " + total_paid)
# print("Remaining balance: " + remaining_balance)



count = 0
total = 0
prev_balance = balance
while count <= 11:
    monthly_interest_rate = annualInterestRate / 12.0
    minimum_monthly_payment = monthlyPaymentRate * prev_balance
    monthly_unpaid_balance = prev_balance - minimum_monthly_payment
    prev_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    count += 1
    total = total + minimum_monthly_payment
    print("Month: " + str(count))
    print("Minimum monthly payment: " + str(round(minimum_monthly_payment, 2)))
    print("Remaining balance: " +str(round(prev_balance, 2)))

print("Total paid: " +str(round(total, 2)))
print("Remaining balance: " +str(round(prev_balance , 2)))
          
