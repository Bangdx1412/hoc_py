# ax + b = 0

# nếu a != 0 -> x = -b/a
# nếu a = 0 :
#          b = 0 -> pt vô số nghiệm
#          b != 0 -> pt vô nghiệm

a = float(input("a = "))
b = float(input("b = "))
x = 0
if a !=0 :
    x = -b/a
    print(x)
else :
    if b==0 :
        print("Pt vô số nghiệm")
    else :
        print ("pt vô nghiệm")
