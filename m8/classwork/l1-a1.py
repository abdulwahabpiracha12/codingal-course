lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List :", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

lst = lst*2
print("Multiplication on List :", lst)

lst = lst[2:5]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)
