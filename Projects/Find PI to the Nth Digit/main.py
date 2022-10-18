# NUMBERS | Find PI to the Nth Digit
import math

isRunning = True

while isRunning:
    n = int(input("Decimal places: "))
    pi = math.pi

    if n == "":
        print("Number cannot be empty.")
        int(input("Decimal places: "))
    elif n <= 0:
        print("Please enter a positive number.")
        int(input("Decimal places: "))
    elif n >= 12:
        print("Number must be smaller than 12.")
        int(input("Decimal places: "))
    else:
        output = round(pi, n)
        print("Rounded Pi: " + str(output))
        isRunning = False
