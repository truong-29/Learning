# Bài 03 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 03

## 📖 1. Kiến thức cơ bản

### 3.1. Toán tử số học

Python tính toán như một chiếc máy tính bỏ túi:

```python
a = 10
b = 3

print(a + b)    # 13   cộng
print(a - b)    # 7    trừ
print(a * b)    # 30   nhân
print(a / b)    # 3.333...  chia (luôn ra số thực float)
print(a // b)   # 3    chia lấy phần nguyên (bỏ phần lẻ)
print(a % b)    # 1    chia lấy phần dư (số dư của phép chia)
print(a ** b)   # 1000 lũy thừa (10 mũ 3)
```

Hai toán tử `//` và `%` rất hữu ích. Ví dụ, `%` giúp kiểm tra một số chẵn hay lẻ: số chẵn thì `n % 2` bằng 0.

### 3.2. Toán tử so sánh

So sánh hai giá trị, kết quả luôn là `bool` (`True` hoặc `False`):

```python
print(5 == 5)    # True   bằng nhau (chú ý: DÙNG HAI dấu bằng)
print(5 != 3)    # True   khác nhau
print(5 > 3)     # True   lớn hơn
print(5 < 3)     # False  nhỏ hơn
print(5 >= 5)    # True   lớn hơn hoặc bằng
print(3 <= 2)    # False  nhỏ hơn hoặc bằng
```

Ghi nhớ quan trọng: `=` là **gán giá trị**, còn `==` là **so sánh bằng nhau**. Đừng nhầm lẫn!

### 3.3. Toán tử logic: `and`, `or`, `not`

Dùng để kết hợp nhiều điều kiện:

- `and` — VÀ: đúng khi **cả hai** vế đều đúng.
- `or` — HOẶC: đúng khi **ít nhất một** vế đúng.
- `not` — PHỦ ĐỊNH: đảo ngược đúng thành sai và ngược lại.

```python
tuoi = 20
co_bang_lai = True

print(tuoi >= 18 and co_bang_lai)   # True  (cả 2 đều đúng)
print(tuoi < 18 or co_bang_lai)     # True  (vế sau đúng là đủ)
print(not co_bang_lai)              # False (đảo ngược True)
```

Ví dụ đời thường: "Được lái xe nếu **đủ 18 tuổi VÀ có bằng lái**" → `tuoi >= 18 and co_bang_lai`.

### 3.4. Nhận dữ liệu từ người dùng — `input()`

Hàm `input()` dừng chương trình lại, chờ người dùng gõ gì đó rồi nhấn Enter. Chuỗi trong ngoặc là lời nhắc hiển thị ra màn hình:

```python
ten = input("Nhập tên của bạn: ")   # chờ người dùng gõ
print("Xin chào,", ten)              # in lời chào
```

**RẤT QUAN TRỌNG:** `input()` luôn trả về **chuỗi** (`str`), kể cả khi người dùng gõ số. Muốn tính toán phải ép kiểu:

```python
tuoi_chu = input("Nhập tuổi của bạn: ")   # ví dụ gõ 20 → nhận "20" (str)
tuoi = int(tuoi_chu)                       # ép sang int để tính
print("Năm sau bạn", tuoi + 1, "tuổi")     # cộng được vì đã là số

# Có thể viết gọn: ép kiểu ngay khi nhập
chieu_cao = float(input("Nhập chiều cao (m): "))   # ép sang float luôn
print("Chiều cao:", chieu_cao)
```

### 3.5. In đẹp bằng f-string

**f-string** là cách in hiện đại và dễ đọc nhất: thêm chữ `f` trước dấu nháy, rồi đặt tên biến trong dấu ngoặc nhọn `{}`. Python sẽ thay biến bằng giá trị của nó.

```python
ten = "An"
tuoi = 20

# Cách cũ (rối): print("Tôi tên " + ten + ", " + str(tuoi) + " tuổi")
# Cách f-string (gọn, rõ):
print(f"Tôi tên {ten}, {tuoi} tuổi.")   # Tôi tên An, 20 tuổi.

# Có thể tính toán ngay trong {}
gia = 20000
sl = 3
print(f"Tổng tiền: {gia * sl} đồng")     # Tổng tiền: 60000 đồng
```
