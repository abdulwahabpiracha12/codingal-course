my_tuple = ()
print(my_tuple)


my_tuple = (1, 2, 3)
print(my_tuple)


my_tuple = (1, "Hello", 3.4, [1,2])
print(my_tuple)


my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)


my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[-1])


n_tuple = ("mouse", [8, 4, 6,(1,2,"abcd",{'1':2})], (1, 2, 3))


print(n_tuple[0][3])
print(n_tuple[1][1])
print(n_tuple[1][3][3]['1'])


print("sliced :", my_tuple[1:4])


for letter in (my_tuple):
    print("Hello", letter)