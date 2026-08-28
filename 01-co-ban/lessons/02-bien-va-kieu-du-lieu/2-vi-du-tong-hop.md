# Bài 02 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 02

## 💡 Ví dụ minh họa tổng hợp

```python
# thong_tin.py — quản lý thông tin một sản phẩm

ten_sp = "Bút bi"          # str: tên sản phẩm
so_luong = 3               # int: số lượng
don_gia = 5000.0           # float: giá mỗi cái
con_hang = True            # bool: còn hàng hay không

# Tính tổng tiền = số lượng * đơn giá
tong_tien = so_luong * don_gia

print("Sản phẩm:", ten_sp)         # dùng dấu phẩy để in nhiều thứ, tự thêm dấu cách
print("Số lượng:", so_luong)
print("Tổng tiền:", tong_tien)     # 15000.0
print("Còn hàng:", con_hang)       # True
print("Kiểu của tong_tien là:", type(tong_tien))   # <class 'float'>
```

Giải thích: ta tạo 4 biến với 4 kiểu khác nhau, nhân số lượng với đơn giá để ra tổng tiền, rồi in tất cả ra. Dấu phẩy trong `print` giúp in nhiều giá trị cách nhau bởi dấu cách mà không cần ép kiểu thủ công.
