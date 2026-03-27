# Xây dựng hàm
# def ten_ham([Ds_tham_so]):
    # ds_cac_lenh
# Tính tổ hợp chập k của n!
# n!/(k! * (n-k)!)
# def GiaiThua (n) : 
#     s = 1
#     for i in range (1,n+1):
#         s *= i
#     return s
# kq = GiaiThua(5)/(GiaiThua(3)*GiaiThua(5-3))
# print(kq)

# Tìm UCLN
def UCLN(a,b):
    if(a>b):
        a,b = b, a
    ucln = 1
    for i in range(a,0, -1):
        if(a%i==0 and b%i ==0):
            ucln = i
            break
    return ucln

print(UCLN(10,25))