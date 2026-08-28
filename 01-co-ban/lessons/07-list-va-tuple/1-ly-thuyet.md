# Bài 07 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 07

## 📖 1. Kiến thức cơ bản

### 1.1. List là gì?

List (danh sách) giống như một **hộp đựng nhiều ngăn**, mỗi ngăn chứa một giá trị và được đánh số thứ tự. Thay vì tạo 5 biến rời rạc cho 5 học sinh, ta gom tất cả vào một list.

```python
# Tạo list bằng cặp ngoặc vuông []
mon_hoc = ["Toán", "Lý", "Hóa"]
diem = [8, 6, 9, 10]
hon_hop = ["Lan", 20, True]   # list chứa nhiều kiểu dữ liệu cũng được
rong = []                     # list rỗng
```

### 1.2. Truy cập phần tử bằng chỉ số (index)

Phần tử được đánh số **từ 0**: phần tử đầu là 0, phần tử thứ hai là 1...

```python
mon_hoc = ["Toán", "Lý", "Hóa"]
print(mon_hoc[0])     # Toán  (phần tử đầu tiên)
print(mon_hoc[2])     # Hóa   (phần tử thứ ba)

# Chỉ số âm đếm từ cuối lên
print(mon_hoc[-1])    # Hóa   (phần tử cuối cùng)
print(mon_hoc[-2])    # Lý
```

### 1.3. Sửa và duyệt list

```python
diem = [8, 6, 9]
diem[1] = 7           # sửa phần tử thứ hai từ 6 thành 7
print(diem)           # [8, 7, 9]

# Duyệt qua từng phần tử bằng for
for d in diem:
    print(d)
```

### 1.4. Thêm và xóa phần tử

```python
gio_hang = ["Táo", "Cam"]

gio_hang.append("Chuối")       # thêm vào CUỐI list
print(gio_hang)                # ['Táo', 'Cam', 'Chuối']

gio_hang.insert(1, "Xoài")     # chèn vào vị trí 1
print(gio_hang)                # ['Táo', 'Xoài', 'Cam', 'Chuối']

gio_hang.remove("Cam")         # xóa phần tử có giá trị "Cam"
print(gio_hang)                # ['Táo', 'Xoài', 'Chuối']

cuoi = gio_hang.pop()          # lấy ra và xóa phần tử cuối
print(cuoi)                    # Chuối
print(gio_hang)                # ['Táo', 'Xoài']
```

### 1.5. Slice — lấy một đoạn của list

Cú pháp `list[start:stop]` lấy các phần tử từ `start` đến `stop - 1`.

```python
so = [10, 20, 30, 40, 50]
print(so[1:3])     # [20, 30]  (vị trí 1 và 2)
print(so[:2])      # [10, 20]  (từ đầu đến vị trí 1)
print(so[3:])      # [40, 50]  (từ vị trí 3 đến hết)
print(so[-2:])     # [40, 50]  (hai phần tử cuối)
```

### 1.6. Các method và hàm phổ biến

```python
so = [3, 1, 4, 1, 5]

print(len(so))     # 5     — số lượng phần tử
print(sum(so))     # 14    — tổng các phần tử
print(max(so))     # 5     — giá trị lớn nhất
print(min(so))     # 1     — giá trị nhỏ nhất
print(so.count(1)) # 2     — đếm số lần xuất hiện của 1

so.sort()          # sắp xếp tăng dần (thay đổi chính list)
print(so)          # [1, 1, 3, 4, 5]

so.reverse()       # đảo ngược
print(so)          # [5, 4, 3, 1, 1]

print("Táo" in ["Táo", "Cam"])  # True — kiểm tra phần tử có trong list
```

### 1.7. Tuple và sự khác biệt

Tuple giống list nhưng dùng ngoặc tròn `()` và **không thể thay đổi** sau khi tạo (gọi là "bất biến" - immutable).

```python
# Tuple dùng ngoặc tròn
toa_do = (10, 20)
print(toa_do[0])   # 10  — truy cập giống list

# toa_do[0] = 5    # LỖI! Không thể sửa tuple
```

Khi nào dùng tuple thay vì list?
- Khi dữ liệu **không nên thay đổi**: tọa độ (x, y), ngày tháng năm, màu RGB.
- Tuple an toàn hơn (không sợ lỡ tay sửa) và chạy nhanh hơn một chút.

| Đặc điểm | List `[]` | Tuple `()` |
|----------|-----------|------------|
| Thay đổi được? | Có | Không |
| Dùng khi | Dữ liệu hay thay đổi | Dữ liệu cố định |
| Có `append`, `sort`? | Có | Không |
