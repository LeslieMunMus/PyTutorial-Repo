import os

os.system("clear")
# We have 3 logical operators True, False and Not

high_income = True
good_credit = False

if high_income and good_credit:  # if both conditions are True
    print("You're eligible for a loan")
elif high_income or good_credit:  # if one condition is True
    print("You're also eligible for a loan with conditions")
else:
    print("Unfortunately you do not qualify")

# We can use comparison operators for boolean expressions
# The operators are <, >, <=, >=, ==, !=

