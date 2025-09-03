import math

print("Regular Polygon Area Calculator")

# User input
n = int(input("Enter number of sides: "))
s = float(input("Enter length of each side: "))

# Formula
area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))

print(f"\nThe area of the polygon is: {area}")