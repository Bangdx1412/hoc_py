tongTien = 10000000

laiHangThang = 0
for i in range(1,61):
    laiHangThang = tongTien * 0.01
    tongTien += laiHangThang
print(tongTien)