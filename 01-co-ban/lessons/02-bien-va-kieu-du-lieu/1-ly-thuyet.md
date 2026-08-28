# Bài 02 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 02

## 📖 1. Kiến thức cơ bản

### 2.1. Biến là gì?

Hãy tưởng tượng **biến** như một chiếc hộp có dán nhãn. Bạn cất một giá trị vào hộp, đặt tên cho hộp, và sau này gọi tên hộp để lấy lại giá trị bên trong.

Trong Python, ta tạo biến bằng dấu `=` (gọi là **phép gán**). Đọc là "gán... cho...":

```python
tuoi = 20              # Tạo hộp tên "tuoi", cất số 20 vào
ten = "An"             # Tạo hộp tên "ten", cất chữ "An" vào

print(tuoi)            # In ra: 20
print(ten)             # In ra: An
```

Lưu ý: `=` trong lập trình KHÔNG phải là "bằng nhau" trong toán học. Nó có nghĩa là "cất giá trị bên phải vào biến bên trái". Bạn có thể thay giá trị bất cứ lúc nào:

```python
diem = 5               # diem đang là 5
diem = 9               # Bây giờ diem là 9 (giá trị cũ bị thay thế)
print(diem)            # In ra: 9
```

### 2.2. Quy tắc đặt tên biến

- Chỉ gồm chữ cái, chữ số và dấu gạch dưới `_`. Ví dụ: `ten`, `so_tuoi`, `diem2`.
- **Không** được bắt đầu bằng chữ số: `2diem` sai, `diem2` đúng.
- **Không** chứa dấu cách: dùng `ho_ten` thay vì `ho ten`.
- Phân biệt hoa/thường: `Tuoi` và `tuoi` là hai biến khác nhau.
- Nên đặt tên có nghĩa: `gia_tien` dễ hiểu hơn `x`.

### 2.3. Các kiểu dữ liệu cơ bản

Mỗi giá trị trong Python có một **kiểu** (loại). Bốn kiểu bạn gặp nhiều nhất:

**`int` — số nguyên** (số không có phần thập phân):

```python
tuoi = 20              # int
so_luong = -5          # int cũng có thể âm
print(tuoi)            # 20
```

**`float` — số thực** (số có phần thập phân, dùng dấu chấm `.`):

```python
chieu_cao = 1.75       # float
gia = 19.99            # float
print(gia)             # 19.99
```

**`str` — chuỗi** (text/chữ, luôn bọc trong dấu nháy `"..."` hoặc `'...'`):

```python
ten = "Nguyễn Văn An"  # str
loi_chao = 'Xin chào'  # str (nháy đơn cũng được)
print(ten)             # Nguyễn Văn An
```

**`bool` — luận lý** (chỉ có 2 giá trị: `True` hoặc `False`, viết hoa chữ đầu):

```python
da_ket_hon = False     # bool
la_sinh_vien = True    # bool
print(la_sinh_vien)    # True
```

### 2.4. Kiểm tra kiểu bằng `type()`

Khi không chắc một giá trị thuộc kiểu gì, dùng hàm `type()`:

```python
print(type(20))        # <class 'int'>
print(type(1.75))      # <class 'float'>
print(type("An"))      # <class 'str'>
print(type(True))      # <class 'bool'>

x = 100
print(type(x))         # <class 'int'>  (kiểm tra kiểu của biến x)
```

Dòng `<class 'int'>` nghĩa là giá trị đó thuộc kiểu `int`.

### 2.5. Ép kiểu (chuyển đổi kiểu dữ liệu)

Đôi khi ta cần biến một giá trị từ kiểu này sang kiểu khác. Dùng các hàm: `int()`, `float()`, `str()`.

```python
# Từ chuỗi số sang số nguyên
tuoi_chu = "25"                # đây là str, KHÔNG tính toán được
tuoi_so = int(tuoi_chu)        # chuyển thành int
print(tuoi_so + 5)             # 30  (giờ mới cộng được)

# Từ số sang chuỗi (để ghép với text)
diem = 9
print("Điểm của bạn là " + str(diem))   # Điểm của bạn là 9

# Từ chuỗi sang số thực
gia_chu = "19.99"
gia_so = float(gia_chu)        # chuyển thành float
print(gia_so)                  # 19.99
```

Vì sao cần ép kiểu? Vì mọi thứ người dùng nhập từ bàn phím (bài sau bạn sẽ học `input()`) đều là **chuỗi** `str`. Muốn tính toán ta phải đổi sang số trước.
