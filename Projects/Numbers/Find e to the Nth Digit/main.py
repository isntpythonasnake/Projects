# NUMBERS | Find e to the Nth Digit
import math

isRunning = True

while isRunning:
    try:
        n = int(input("Decimal places: "))
    except ValueError:
        print("Number cannot be empty and must be an integer.")
    else:
        e = math.e

        if n <= 0:
            print("Enter a positive number.")
            int(input("Decimal places: "))
        elif n >= 12:
            print("Number must be smaller than 12.")
            int(input("Decimal places: "))
        else:
            output = round(e, n)
            print("Rounded e: " + str(output))
            isRunning = False
