# tháng 2 năm nhuận có 29 ngày
# tháng 2 bình thường có 28 ngày
# Năm nhuận là năm chia hết cho 4 mà không chia hết cho 100 hoặc là chia hết cho 400

month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))



if(month == 1 or month == 3 or month == 5 or month == 7 or month ==  8 or month == 10 or month == 12):
    print('Tháng',month,' này có 31 ngày')
else : 
    if(month == 2):
        if((year%4 == 0 and year %100 !=0 ) or year %400 == 0):
            print('Tháng',month,' này có 29 ngày')
        else:
            print('Tháng',month,' này có 28  ngày')
    else :
        print('Tháng',month,' này có 30 ngày')
            