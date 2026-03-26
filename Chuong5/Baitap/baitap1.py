import math

x = int(input("X = "))
n =  int(input("n = "))
s = 0
for i in range(2,2 * n + 1,2):
    s+=math.pow(x,i)

print(s)