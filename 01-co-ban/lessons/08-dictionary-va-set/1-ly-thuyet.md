# Bài 08 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 08

## 📖 1. Kiến thức cơ bản

### 1.1. Dictionary là gì?

Dictionary (từ điển) giống như một **cuốn danh bạ điện thoại**: bạn tra "tên" (key) để tìm ra "số điện thoại" (value). Thay vì đánh số thứ tự như list, dictionary dùng **tên khóa** để truy cập giá trị.

```python
# Tạo dictionary bằng cặp ngoặc nhọn {}, mỗi cặp là key: value
hoc_sinh = {
    "ten": "Lan",
    "tuoi": 16,
    "lop": "10A"
}
rong = {}          # dictionary rỗng
```

### 1.2. Truy cập giá trị bằng key

```python
hoc_sinh = {"ten": "Lan", "tuoi": 16}

print(hoc_sinh["ten"])         # Lan
print(hoc_sinh["tuoi"])        # 16

# Dùng get() an toàn hơn: không có key thì trả về None thay vì báo lỗi
print(hoc_sinh.get("lop"))     # None
print(hoc_sinh.get("lop", "Chưa có"))  # Chưa có (giá trị mặc định)
```

### 1.3. Thêm, cập nhật và xóa

```python
hoc_sinh = {"ten": "Lan", "tuoi": 16}

hoc_sinh["lop"] = "10A"        # thêm key mới
hoc_sinh["tuoi"] = 17          # cập nhật value của key đã có
print(hoc_sinh)                # {'ten': 'Lan', 'tuoi': 17, 'lop': '10A'}

del hoc_sinh["lop"]            # xóa cặp key-value
print(hoc_sinh)                # {'ten': 'Lan', 'tuoi': 17}

print("ten" in hoc_sinh)       # True — kiểm tra key có tồn tại
```

### 1.4. Duyệt qua dictionary

```python
diem = {"Toán": 8, "Lý": 7, "Hóa": 9}

# Duyệt qua các key
for mon in diem:
    print(mon)                 # Toán, Lý, Hóa

# Duyệt qua cả key và value bằng items()
for mon, so_diem in diem.items():
    print(f"{mon}: {so_diem}")

# Chỉ lấy value
print(list(diem.values()))     # [8, 7, 9]
# Chỉ lấy key
print(list(diem.keys()))       # ['Toán', 'Lý', 'Hóa']
```

### 1.5. Set là gì?

Set (tập hợp) là một nhóm các phần tử **không trùng lặp** và **không có thứ tự**. Giống như một túi bi mà mỗi màu chỉ có đúng một viên.

```python
# Tạo set bằng ngoặc nhọn {} (nhưng chỉ có giá trị, không có key)
mau = {"đỏ", "xanh", "vàng"}

# Thêm phần tử trùng sẽ bị bỏ qua
mau.add("đỏ")
print(mau)                     # vẫn chỉ 3 phần tử

mau.add("tím")                 # thêm phần tử mới
mau.remove("xanh")             # xóa phần tử
print(len(mau))                # số phần tử hiện có
```

Lưu ý: set rỗng phải tạo bằng `set()`, không phải `{}` (vì `{}` là dictionary rỗng).

### 1.6. Ứng dụng của set

Ứng dụng phổ biến nhất là **loại bỏ trùng lặp** trong list:

```python
so = [1, 2, 2, 3, 3, 3, 4]
so_khong_trung = set(so)       # chuyển thành set
print(so_khong_trung)          # {1, 2, 3, 4}
print(list(so_khong_trung))    # đổi ngược lại thành list nếu cần
```

Set còn hỗ trợ các phép toán tập hợp như trong toán học:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # hợp: {1, 2, 3, 4, 5, 6}
print(a & b)   # giao (phần chung): {3, 4}
print(a - b)   # hiệu (có trong a, không trong b): {1, 2}
```
