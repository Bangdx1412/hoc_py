import math
# Bài 1. Viết chương trình C để tính cước điện thoại bàn cho một hộ gia đình với các thông số như sau:

#             Phí thuê bao bắt buộc là 25 nghìn.
phiThue = 25000

#             600 đồng cho mỗi phút gọi của 50 phút đầu tiên.
phut_50 = 600
#             400 đồng cho mỗi phút gọi của 150 phút tiếp theo.
phut_51_150 = 400
#             200 đồng cho bất kỳ phút gọi nào sau 200 phút đầu tiên.
phut_201 = 200

def tinhTien(so_phut_goi) :
    kq = 0
    if so_phut_goi<=50:
        kq = so_phut_goi*phut_50 +phiThue
    elif so_phut_goi >50 and so_phut_goi<=200: 
        kq = 50*phut_50 + (so_phut_goi-50) * phut_51_150 +phiThue
    else:
        kq = 50*phut_50 + 150 * phut_51_150 + (so_phut_goi-200) * phut_201 + phiThue
        
    print(kq)
    
tinhTien(10)