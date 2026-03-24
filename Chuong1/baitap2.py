dien_ke = 1000
kw_50 = 230
vuot_50 = 480
kw_100 = 700
vuot_100 = 900


def soDien(soDienCu, soDienMoi):

    if soDienMoi < soDienCu:
        print("Sai số điện")
        return

    dien_su_dung = soDienMoi - soDienCu

    tien_dm = 0
    tien_vuot = 0

    if dien_su_dung <= 50:
        tien_dm = dien_su_dung * kw_50

    elif dien_su_dung <= 100:
        tien_dm = 50 * kw_50
        tien_vuot = (dien_su_dung - 50) * vuot_50

    elif dien_su_dung <= 150:
        tien_dm = 50 * kw_50
        tien_vuot = 50 * vuot_50 + (dien_su_dung - 100) * kw_100

    else:
        tien_dm = 50 * kw_50
        tien_vuot = 50 * vuot_50 + 50 * kw_100 + (dien_su_dung - 150) * vuot_100

    tong = tien_dm + tien_vuot + dien_ke

    print("Chỉ số cũ:", soDienCu)
    print("Chỉ số mới:", soDienMoi)
    print("Tiền định mức:", tien_dm)
    print("Tiền vượt định mức:", tien_vuot)
    print("Tổng tiền:", tong)


soDien(100, 150)