#break
# nhập vào các số dương, tính tổng các số dương vừa nhập , nếu mà gặp số âm thì thoát và inra tổng các số dương vừa nhập vào
s = 0
while(True):
    n = int(input("Nhập n= "))
    if n<0 :
        break
    s+=n

print(s)

    