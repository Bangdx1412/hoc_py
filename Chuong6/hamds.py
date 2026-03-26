# Nhập vào n phần tử trong dnah sách và tính tổng

# tinh tông
# sum(danhsach)
# Lấy độ dài danh sách
a = []
n = int(input("Nhập n phần tử:"))
for i in range(0,n) :
    x = int(input("Nhập các phần từ"))
    a.append(x)
count = len(a)
print(count)
tong = sum(a)
# print(tong)

# sorted sắp xếp theo thứ tự tăng dần
c = sorted(a)
print(c)
# c = sorted(<danh sách>,reverse=True) Xắp sếp giảm dần
d = sorted(a,reverse=True)
print(d)
print(max(a))
print(min(a))
