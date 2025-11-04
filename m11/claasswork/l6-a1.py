
import math;

def printPowerSet(set, SetSize):


    PowerSetSize = (int)(math.pow(2, SetSize))

    for outer in range(0, PowerSetSize):
        print("{", end = "")
        for inner in range(0, SetSize):


            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("}")

size = int(input("Enter array size :"))

lst = []
for i in range(0, size):
    n = int(input(f"Enter element no {i+1}: "))
    lst.append(n)

printPowerSet(lst, len(lst))