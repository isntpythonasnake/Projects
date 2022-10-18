interval = input("Enter the interval of your mortgage payments(Monthly, Weekly, Daily, Annually): ")
loan = float(input("Enter your loan amount: "))
n = int(input("Amount of intervals: "))
interest = float(input("Interest rate: "))
i = interest / 100

if interval == "Daily":
    daily = loan / n * i / 31
    print(daily)
elif interval == "Weekly":
    weekly = loan / n * i / 4
    print(weekly)
elif interval == "Monthly":
    monthly = loan / n * i
    print(monthly)
elif interval == "Annually":
    annually = loan / n * i * 12
    print(annually)
else:
    print("Please enter either Monthly, Weekly, Daily, or Annually!")