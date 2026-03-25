# gặp continute quay lại vòng lập thực hiện tiếp
# i = 1
# while(i<=10) : 
#     i+=1
#     print('hehe')
#     continue
#     print("Hello")

# Tính tổng các số chẵn từ 1-n 
n = int(input("n = "))
i = 1
kq = 0
for i in range(1,n+1):
    if(i % 2 ==1):
        continue
    kq = kq+i
print(kq)