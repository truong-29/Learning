# Bài 03 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 03

## 💡 Ví dụ minh họa tổng hợp

```python
# may_tinh.py — máy tính cộng hai số do người dùng nhập

print("=== MÁY TÍNH CỘNG ===")

# Nhận 2 số từ người dùng, ép sang float để tính được cả số lẻ
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))

# Tính toán
tong = so1 + so2
hieu = so1 - so2
tich = so1 * so2

# In kết quả bằng f-string
print(f"{so1} + {so2} = {tong}")
print(f"{so1} - {so2} = {hieu}")
print(f"{so1} x {so2} = {tich}")
```

Nếu người dùng nhập `5` và `3`, output sẽ là:

```
=== MÁY TÍNH CỘNG ===
Nhập số thứ nhất: 5
Nhập số thứ hai: 3
5.0 + 3.0 = 8.0
5.0 - 3.0 = 2.0
5.0 x 3.0 = 15.0
```

Giải thích: ta dùng `float(input(...))` để vừa nhận vừa ép kiểu, tính 3 phép, rồi dùng f-string in kết quả gọn gàng.
