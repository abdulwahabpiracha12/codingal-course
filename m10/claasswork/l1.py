import time

#Most efficent: Irrespective of the value of n the number of iterations is just 1.
def fun1(n):
  return n*(n+1)/2

#As the value of n increases so does the number of iterations increases.
def fun2(n):
  sum = 0
  for i in range(1, n+1) :
      sum += i
  return sum

#Least efficent: The number of iterations increase at a faster pace than the value of n itself
def fun3(n):
    sum = 0
    for i in range(1, n+1):
       for j in range(i, i+1):
          sum += 1
    return sum

n = 1000
fun1(n)
fun2(n)
fun3(n)