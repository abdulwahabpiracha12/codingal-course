
with open('codingal.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")


 
with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print(data)
    print("Words in this file are...")
    for line in data:
      word = line.split()
      print(word)