s = "hoc python"
# capitalize(): In hoa chữ đầu tiên trong chuỗi
print(s.capitalize())

# upper() Chuyển toàn bộ chuỗi sang chữ in hoa
print(s.upper())

# lower() : Chuyển từ chữ hoa sang chữ thường
print(s.lower())

# title() Chuyển kí tự đầu mỗi từ sang in hoa
print(s.title())

# strip() Xóa kí tự được chỉ định ở đầu và cuối chuỗi
a="     hehe****"
print(a.strip())
# len(a): Đếm số kí tự
print(len(a.strip()))

# lstrip() Xóa kí tự được chỉ định ở bên trái của chuỗi
ls="MiHoa"
print(ls.lstrip("M"))

# split(): Tách các kí tự trong chuỗi 
# chuoi.split(char,n)

s1 = "Tuyệt đỉnh kung fu"
print(s1.split(" ", -1))
print(s1.split(" ", 2))
print(s1.split())

# count("",start, end) : Đếm số lần xuất hiện của một chuỗi con trong chuỗi gốc
s2 = "Hello Hello hello word"
s3 = s2.lower()
print(s3.count("hello"))

# find("chuoi can tìm", start, end) :Tìm chuỗi con trong chuỗi gốc, nếu k tìm được thì trả về -1
print(s2.find("he"))

# join(): Nối chuỗi
#  ky_tu_noi.join(Tham_so)
q = ["Hoc","Python"]
y = " ".join(q)
print(y)

# replace("chuoi_thay","chuoi_moi", số lần thay) Thay thế 1 chuỗi con trong chuỗi gốc
t = "xin chao moi nguoi, moi nguoi khỏe không"
print(t.replace("moi nguoi", "thế giới",1))

