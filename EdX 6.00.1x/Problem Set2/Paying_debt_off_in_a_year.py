# Paying Debt Off in a Year
# Author: Enes Kemal Ergin

'''Now write a program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay
off all debt in under 1 year, for example:

Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance at
the end of the month (after the payment for that month is made).
The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using
this payment scheme, which is okay. A summary of the required math
is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) +
    (Monthly interest rate x Monthly unpaid balance)
'''




def paying_debt(balance, annualInterestRate):
    monthly_payment = 10
    monthly_interest_rate = annualInterestRate / 12.0
    updated_balance = balance - 10

    while updated_balance > 0:
        monthly_payment += 10
        updated_balance = balance
        count = 0
        while count < 12 and updated_balance >0:
            interest = monthly_interest_rate * updated_balance
            updated_balance -= monthly_payment
            updated_balance += interest
            count += 1

    print("Lowest Payment: " + str(monthly_payment))

print(paying_debt(3329, 0.2))
print(paying_debt(4773, 0.2))   # Wrong
print(paying_debt(3926, 0.2))   # Wrong
print(paying_debt(839, 0.18))
print(paying_debt(763, 0.25))
print(paying_debt(536, 0.18))
print(paying_debt(749, 0.2))
print(paying_debt(3632, 0.2))
print(paying_debt(3527, 0.04))  # Wrong
print(paying_debt(3665, 0.04))
print(paying_debt(4984, 0.04))
print(paying_debt(4289, 0.04))
print(paying_debt(3781, 0.15))  # Wrong
print(paying_debt(3701, 0.15))  # Wrong
print(paying_debt(4064, 0.04))
