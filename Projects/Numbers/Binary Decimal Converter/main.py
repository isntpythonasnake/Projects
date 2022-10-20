isRunning = True
bord = str(input("Enter Binary or Decimal to convert to: "))

while isRunning:
    if bord == "Decimal":
        b = int(input("Decimal to convert to Binary: "))
        bn = bin(b)
        print(str(bn).replace("0b", "Answer: "))
        break
    elif bord == "Binary":
        d = input("Binary to convert to Decimal: ")
        dn = int(d, 2)
        print("Answer: " + str(dn))
        break
    elif bord != "Decimal" or bord != "Binary":
        print("Please enter either Binary or Decimal!")
        bord = str(input("Enter Binary or Decimal to convert to: "))

