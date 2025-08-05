num = int(input("Enter the number"))
print(f"Table of {num}")
for i in range(1,11):
    mu1 = num*i
    print("%d x %d = %d" % (num,i, mu1))