# while(<dieu_kien>): #trong khi điều kiện còn đúng thì thực hiện các câu lệnh trong while
    # <cac_lenh>
# i = 0
# while(i<10):
#     print(i)
#     i+=1

# Tính n! với n nhập từ bàn phím
n = int(input("n= "))
i = 1
s = 1
while i <= n:
    s *= i
    i += 1
print(s)
