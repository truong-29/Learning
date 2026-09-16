print("--- 1 ---")

chieu_dai = 5.0          # mét (float)
chieu_rong = 4.0         # mét (float)
chieu_cao = 3.0          # mét (float)
dien_tich_cua_so = 5.5   # m2 phần tường KHÔNG sơn (float)
gia_moi_m2 = "25000"     # chuỗi (str), đơn vị đồng/m2
so_nguoi_chia_tien = "2" # chuỗi (str)

dien_tich_tuong = 2*(chieu_dai + chieu_rong)*chieu_cao
dien_tich_can_son = dien_tich_tuong - dien_tich_cua_so
gia_moi_m2_int = int(gia_moi_m2)
tong_chi_phi = dien_tich_can_son * gia_moi_m2_int
so_nguoi_chia_tien_int  = int(so_nguoi_chia_tien)
chi_phi_moi_nguoi = tong_chi_phi / so_nguoi_chia_tien_int
print(type(dien_tich_can_son))
print(type(tong_chi_phi))
print("diện tích bốn bức tường: ", dien_tich_tuong)
print("diện tích cần sơn: ", dien_tich_can_son)
print("tổng chi phí: ", tong_chi_phi)
print("chi phí mỗi người: " + str(chi_phi_moi_nguoi))

print("--- 2 ---")

chuoi_a = "3.5"
chuoi_b = "10"
print(type(chuoi_a))
print(type(chuoi_b))
chuoi_a = float(chuoi_a)
chuoi_b = int(chuoi_b)
tong = chuoi_a + chuoi_b
print("Tổng: ", tong)
print(type(tong))

print("--- 3 ---")
can_nang = 68
chieu_cao = 1.70

BMI = can_nang/(chieu_cao*chieu_cao)
print("Chi so BMI cua ban la: "+ str(BMI))
print(type(BMI))
