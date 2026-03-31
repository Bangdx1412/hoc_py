# 1 MỘT trương trình làm việc với tệp cần 3 bước
# Mở tạo tệp
# đọc ghi dữ liệu vào tệp
# đóng tệp để các tài nguyên được giải phóng

# 2 mở tệp
# ten_bien_tep = open(file_name, mode, encoding)
# Mode: 
#     r : mở ở chế độ mặc định, nếu mà không có thì sẽ báo lỗi
#     w : Mở tệp để ghi dữ liệu vào tệp, nếu tệp chưa tồn tại thì tạo tệp mới, nếu tồn tại rồi
#     thì ghi đè
#     x: Mở tệp nếu chưa tồn tại thì phát sinh lỗi
#     a : mở tệp, để ghi dữ liệu vào tệp, nếu tệp chưa tồn tại thì sẽ tạo tệp, và ghi vào cuối tệp
#     t : mở chế độ văn bản


file = open("Chuong9/SinhVien.txt",'w', encoding="utf-8")

file.write("Di ha noi that met")
file.close()


s= ["Khi mà không còn yêu thì ","Đêm nào ta cũng say vì"]
file2 = open("Chuong9/BanhMiKhong.html",'a',encoding="utf-8")

file2.writelines(s)
file2.close()

file2 = open("Chuong9/BanhMiKhong.html","r",encoding="utf-8")
r = file2.read(10)
print(r)