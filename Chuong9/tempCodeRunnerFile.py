with open("Chuong9/SinhVien.txt") as file :
    s = file.read()
    print(s)
with open("Chuong9/SinhVien.txt","w",encoding="utf-8") as file2:
    ma = input("MÃ: ")
    ten = input("Họ và tên: ")
    file2.writelines([ma,ten])
    