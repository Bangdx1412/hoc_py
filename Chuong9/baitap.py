with open("Chuong9/SinhVien.txt","r", encoding="utf-8") as file :
    r = file.read()
    print(r)
# with open("Chuong9/SinhVien.txt","w",encoding="utf-8") as file2:
#     ma = input("MÃ: ")
#     ten = input("Họ và tên: ")
#     file2.writelines([ma,ten])
    
# Đọc danh sách
with open("Chuong9/SinhVien.txt", "r", encoding="utf-8") as file3:
    s = file3.read() # Thêm dấu () ở đây
    print("\nDanh sách sau khi cập nhật:")
    print(s)