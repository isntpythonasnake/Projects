w = float(input("Width of floor: "))
h = float(input("Height of height: "))
cost = float(input("Cost of 1 tile: "))
totalcost = w * h * cost
area = w * h

print("Area of the room: " + str(area))
print("Total cost of tiles: $" + str(totalcost))
