# Bài 09 — Xử lý chuỗi · Lý thuyết

> Track: Cơ bản (Beginner) · Module 1 · Bài 09

## 📖 1. Kiến thức cơ bản

### 1.1. Chuỗi là gì?
Chuỗi (string) là một dãy các ký tự đặt trong dấu nháy đơn `'...'` hoặc nháy kép `"..."`. Bạn hãy tưởng tượng chuỗi giống như một "chuỗi hạt cườm", mỗi hạt là một ký tự và được đánh số thứ tự.

```python
ten = "Nguyen Van An"   # chuỗi trong nháy kép
mon_hoc = 'Python'       # chuỗi trong nháy đơn
print(type(ten))         # <class 'str'>  → kiểu dữ liệu là str (string)
```

### 1.2. Index — truy cập từng ký tự
Mỗi ký tự trong chuỗi có một vị trí (index). Vị trí **bắt đầu từ 0**, không phải 1. Số âm đếm ngược từ cuối.

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5     ← index từ trái
#   -6 -5 -4 -3 -2 -1     ← index từ phải

print(s[0])    # P   → ký tự đầu tiên
print(s[5])    # n   → ký tự thứ 6
print(s[-1])   # n   → ký tự cuối cùng
print(len(s))  # 6   → độ dài chuỗi (số ký tự)
```

> ⚠️ Chuỗi là **bất biến** (immutable): bạn không thể đổi một ký tự trong chuỗi bằng `s[0] = "J"`. Muốn thay đổi, phải tạo chuỗi mới.

### 1.3. Slice — cắt lát chuỗi
Cú pháp: `s[bắt_đầu:kết_thúc]`. Lấy từ vị trí `bắt_đầu` đến **trước** `kết_thúc` (không lấy ký tự ở `kết_thúc`).

```python
s = "Python"
print(s[0:3])   # Pyt   → lấy index 0, 1, 2
print(s[2:])    # thon  → từ index 2 đến hết
print(s[:4])    # Pyth  → từ đầu đến trước index 4
print(s[-3:])   # hon   → 3 ký tự cuối
print(s[:])     # Python → cả chuỗi
print(s[::2])   # Pto   → lấy cách 1 (bước nhảy 2)
print(s[::-1])  # nohtyP → đảo ngược chuỗi (mẹo hay dùng)
```

### 1.4. Các method phổ biến
Method là "hành động" gắn với chuỗi, viết theo dạng `chuoi.ten_method()`. Các method này **không đổi chuỗi gốc** mà **trả về chuỗi mới**.

```python
s = "  Xin Chao Python  "

print(s.upper())        # '  XIN CHAO PYTHON  '  → viết HOA hết
print(s.lower())        # '  xin chao python  '  → viết thường hết
print(s.strip())        # 'Xin Chao Python'      → bỏ khoảng trắng 2 đầu
print(s.replace("o", "0"))  # thay mọi 'o' thành '0'
print("Python".find("th")) # 2  → vị trí đầu tiên tìm thấy "th" (không thấy trả về -1)
print("Python".find("z"))  # -1 → không tìm thấy
```

`split()` tách chuỗi thành **list**, `join()` ghép list thành **chuỗi**:

```python
cau = "toi thich hoc python"
tu = cau.split()          # ['toi', 'thich', 'hoc', 'python'] → tách theo khoảng trắng
print(tu)

ngay = "25-08-2026"
phan = ngay.split("-")    # ['25', '08', '2026'] → tách theo dấu '-'
print(phan)

danh_sach = ["An", "Binh", "Chi"]
ket_qua = ", ".join(danh_sach)  # 'An, Binh, Chi' → ghép bằng dấu ', '
print(ket_qua)
```

Một số method kiểm tra hữu ích (trả về `True`/`False`):

```python
print("Python3".isalnum())   # True  → chỉ gồm chữ và số
print("12345".isdigit())     # True  → toàn chữ số
print("Xin Chao".startswith("Xin"))  # True  → bắt đầu bằng "Xin"
print("bao_cao.txt".endswith(".txt")) # True  → kết thúc bằng ".txt"
```

### 1.5. Định dạng chuỗi (f-string)
Cách hiện đại và dễ đọc nhất để chèn biến vào chuỗi: thêm chữ `f` trước dấu nháy, rồi đặt biến trong `{ }`.

```python
ten = "An"
tuoi = 20
print(f"Xin chao {ten}, ban {tuoi} tuoi.")   # Xin chao An, ban 20 tuoi.

# Có thể tính toán ngay trong dấu ngoặc
gia = 15000
so_luong = 3
print(f"Tong tien: {gia * so_luong} dong")   # Tong tien: 45000 dong

# Làm tròn số thập phân với :.2f  (2 chữ số sau dấu phẩy)
diem = 8.6666
print(f"Diem trung binh: {diem:.2f}")         # Diem trung binh: 8.67
```

---

⬅️ Quay lại [Mục lục bài](README.md) · ➡️ Tiếp theo: [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md)
