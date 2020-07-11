import os

os.system("clear")

""" 
This is a basic while loop
i = 1

while i <= 5:
    print(i)
    i = i + 1
print("Done")
"""

# The weight converter using while loop for error handling this time
# This is the equivalent of C++ do...while loop

while True:
    weight = float(input("Enter weight: "))
    unit = input("Enter 'L' for Lbs or 'K' for Kg: ")

    if unit.upper() == "K":
        calc = weight / 0.45
        print("You weigh %0.2f pounds" % (calc))
        break
    elif unit.upper() == "L":
        calc = weight * 0.45
        print("You weigh %0.2f kilograms" % (calc))
        break
    else:
        if unit.upper() != "K" or unit.upper() != "L":
            print("You have entered a wrong metric unit. Please try again.")

