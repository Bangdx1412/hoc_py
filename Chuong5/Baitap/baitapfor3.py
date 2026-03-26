import math
a = int(input('a = '))
b = int(input('b = '))

if a < b : 
    a,b = b,a
for i in range (b,0,-1):
    if(a%i==0 and b%i == 0):
        ucln = i
        break
print(ucln)
c = math.gcd(a,b)
print(c)

# gcd Lấy ucln
# lcm lấy bcnn