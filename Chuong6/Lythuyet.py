# Kiểu dữ liệu danh sách list

# a = []
# print(type(a))

# b = list()
# print(type(b))


# ten_danh_sach[start:end, step]
a = [8,1,23,45]
# <Ten_danh_sach>.append()  thêm thằng con
a.append(1000)
# ten_danh_sach.insert(i,gtThem)
a.insert(2,12)
# Xóa 1 phần tử
# tenDS._delItem_(index)
a.__delitem__(0)
# tenDS.remove(<Giatrican xoa>) //Xóa phần tử trrong danh sách
a.remove(23)


# Nhập danh sách từ bàn phím 
# khởi tạo một danh sách rỗng5
b = []
n = int(input("n = "))
for i in range(n):
    x = int(input())
    b.append(x)
for value in b:
    print(value)
print(b)