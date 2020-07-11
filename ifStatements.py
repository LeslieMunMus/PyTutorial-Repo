import os

os.system("clear")

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day. Drink lots of water.")
# elif is_cold:
#     print("It's a cold day. Dress warmly.")
# else:
#     print("It's a lovely day!")

temp = float(input("Enter the current temperature in degrees celcius: "))

if temp < 10.0:
    print("It's cold. Dress warmly")
elif temp > 25.0:
    print("It's hot. Drink lots of water")
else:
    print("It's a lovely day")

# if a client has good credit they should put down 10% deposit
#   otherwise they put down a 20% deposit for a R1M house
price = 1000000
good_credit = True

if good_credit:
    print("You have good credit and need to put down a 10% deposit")
    deposit = price * 0.10
    print(f"Your down payment is R{deposit}")
else:
    print("You have bad credit and need to put down a 20% deposit")
    deposit = price * 0.20
    print(f"Your down payment is R{deposit}")
