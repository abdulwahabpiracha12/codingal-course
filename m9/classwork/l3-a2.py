'''
the 'x' mode 




'''

new_file = open('my_file.txt', 'x')
new_file.close()


import os
print("Checking if my_file exst or not....")
if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
  print("my_file.txt is removed!")
else:
  print("The file does not exist")


  my_file = open("my_file.txt", "w")
  my_file.write("Hi! I am Penguin and I am 1 yr old")
  my_file.close()


  os.remove('my_file.txt')

  