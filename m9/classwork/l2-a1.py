
file = open('codingal.txt','r')
print(file.read())
file.close()


file = open('codingal.txt','r')
print("\nRead in parts \n")
print(file.read(8))
file.close()


file = open('codingal.txt','a')
file.write(" Hi! I am Penguin and I am 1 yr old")
file.close()