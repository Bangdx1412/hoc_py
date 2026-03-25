# Cấu trúc lặp for
# for <ten_bien> in <tap_hop> : 
#     <lenh_trong_for>

s = "hello"
# for i in s :
    # print(i)
    

# lệnh range(start, end, step)
# for s1 in range(1,10,1) : # nếu s1 = 10 => Dừng vòng lặp
#     print(s1)

# s = 1 + 2+ 3+4+... n 
n = int(input("Nhập n:"))
kq = 0
for s in range(1,n,1) :
    kq +=s
    
print(kq) 