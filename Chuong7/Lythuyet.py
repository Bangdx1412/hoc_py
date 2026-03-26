# Kiểu từ điển dict key: value
thongtinsinhvien = {
    "MaSV":"PH55741",
    "HoVaTen":"Do XUAN BANG",
    "old":21
}
# tenbien[key]
# tenbien.get(key)
print((thongtinsinhvien["HoVaTen"]))
print(thongtinsinhvien.get("old"))

# tenbien.values()
#tenbien.key()
print(thongtinsinhvien.keys())

# duyet qua cac phần tử trong dict 
# for i in thongtinsinhvien:
#     print(i,":", thongtinsinhvien[i])
    
# Nhập giá trị cho kiểu từ điển
# thongTin = {}
# n = int(input("Nhập n = "))
# for i in range(n) :
#     keys = input()
#     values = input()
#     thongTin[keys] = values
    
# print(thongTin)

# Xóa phần tử theo key
# tenbien.__delitem__(key)
# thongtinsinhvien.__delitem__("HoVaTen")
# for i in thongtinsinhvien : 
#     print(i,":", thongtinsinhvien[i])
# print(thongtinsinhvien)

# tenbien.clear
thongtinsinhvien.clear()
print(thongtinsinhvien)