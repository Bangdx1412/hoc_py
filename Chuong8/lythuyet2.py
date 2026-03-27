# # Chuyền tham số với giá trị batw3s buộc
# def HoanVi(a,b) :
#     a,b = b,a
#     return a,b

# def main() :
#     print(HoanVi(10,20))
    
# main() 

# Truyền tham số với giá trị mặc định 
# import math
# def DienTichHinhTron(r=0):
#     s = math.pi * r*r
#     return s

# def main():
#     print("Dien Tich Hinh Tron:", round(DienTichHinhTron(4),2))
    
# main()


# truyền tham số là từ khóa

# def tinhDienTichHCN (a,b):
#     s= a * b
#     return s
# def main() :
#     print("Diện tích hình chữ nhật là: ", tinhDienTichHCN(a = 4,b=5))
# main()

# truyền giá trị tùy ý
# Tìm giá trị lớn nhất trong các giá trị nhập vào từ bàn phím
def maxGT(*a) :
    n = len(a)
    if(n == 0) :
        return
    else:
        max = a[0]
        for i in range(1,n):
            if(max<a[i]):
                max = a[i]
        return max
    
def main():
    print("Gía trị lớn nhất là: ",maxGT(2,3,4,5))
    
main()