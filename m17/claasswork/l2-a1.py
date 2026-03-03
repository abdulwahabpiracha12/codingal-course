# Create the two sets of two guest lists
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find the union of the two sets
union_set = set1.union(set2)

# converting set into list
# to find total guests to be invited in the party
total_guests = list(union_set)

print("Total guests to be invited in the party are: ", len(total_guests))
print("Guest List :", total_guests)