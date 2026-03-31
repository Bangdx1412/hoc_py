class SinhVien:
    def __init__(self,hoTen, queQuan, lop, diemPyThon, diemTKWeb):
        self.hoTen = hoTen
        self.queQuan = queQuan
        self.lop = lop
        self.diemPyThon = diemPyThon
        self.diemTKWeb = diemTKWeb
    def tinhDiemTB(self) :
        dtb = (self.diemPyThon * 4 + self.diemTKWeb*5)/9
        return dtb
    
    def xepLoai(self,dtb):
       def xepLoai(self, dtb):
        if dtb == 10:
            return "Xuat xac me luon" 
        else:
            return "Kha/Gioi"
dsSV = []
sv1 = SinhVien("Bang", "Ha Nam", "12A3",10,10)
sv2 = SinhVien("Thuy","Thanh Hoa", "12A7",10,10)

print(sv1.hoTen,sv1.tinhDiemTB(),sv1.xepLoai(sv1.tinhDiemTB()))
print(sv2.hoTen,sv2.tinhDiemTB(),sv2.xepLoai(sv1.tinhDiemTB()))
dsSV.append(sv1)
dsSV.append(sv2)

print(dsSV[0].hoTen)