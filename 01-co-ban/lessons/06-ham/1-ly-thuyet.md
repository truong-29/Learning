# Bài 06 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 06

## 📖 1. Kiến thức cơ bản

### 1.1. Hàm là gì?

Hàm giống như một **chiếc máy xay sinh tố**: bạn bỏ nguyên liệu vào (đầu vào), máy xử lý, rồi trả ra ly sinh tố (đầu ra). Bạn không cần biết bên trong máy hoạt động ra sao mỗi lần dùng — chỉ cần bấm nút.

Trong lập trình, hàm là **một khối lệnh có tên**, viết một lần và dùng lại nhiều lần. Điều này giúp code ngắn gọn và tránh lặp lại.

### 1.2. Định nghĩa và gọi hàm

```python
# Định nghĩa hàm bằng từ khóa def
def chao_hoi():
    print("Xin chào!")
    print("Chúc bạn học tốt!")

# Gọi (chạy) hàm — có thể gọi nhiều lần
chao_hoi()
chao_hoi()
```

Lưu ý: chỉ định nghĩa hàm thôi thì chưa có gì xảy ra. Phải **gọi** hàm bằng cú pháp `ten_ham()` thì các lệnh bên trong mới chạy.

### 1.3. Tham số (parameters) — truyền dữ liệu vào hàm

```python
# name là tham số: dữ liệu mà hàm nhận vào
def chao(name):
    print(f"Xin chào, {name}!")

chao("Lan")        # Xin chào, Lan!
chao("Bình")       # Xin chào, Bình!
```

Có thể có nhiều tham số:

```python
def cong(a, b):
    print(f"{a} + {b} = {a + b}")

cong(3, 5)         # 3 + 5 = 8
```

### 1.4. `return` — trả kết quả ra khỏi hàm

`print` chỉ **hiển thị** ra màn hình. `return` thì **trả về một giá trị** để ta dùng tiếp (lưu vào biến, tính toán...).

```python
def cong(a, b):
    return a + b        # Trả về kết quả, KHÔNG in ra

ket_qua = cong(3, 5)    # Lưu giá trị trả về vào biến
print(ket_qua)          # 8
print(cong(10, 20))     # 30 — dùng trực tiếp kết quả
```

Sự khác biệt quan trọng:
- Hàm dùng `print` chỉ để xem, không tái sử dụng kết quả được.
- Hàm dùng `return` cho ta giá trị để tính tiếp, ví dụ `cong(1, 2) + cong(3, 4)`.

Khi gặp `return`, hàm **kết thúc ngay lập tức**:

```python
def kiem_tra_chan(so):
    if so % 2 == 0:
        return "Số chẵn"
    return "Số lẻ"         # Dòng này chỉ chạy nếu điều kiện trên sai

print(kiem_tra_chan(4))    # Số chẵn
print(kiem_tra_chan(7))    # Số lẻ
```

### 1.5. Tham số mặc định (default parameters)

Bạn có thể gán sẵn giá trị cho tham số. Nếu người gọi không truyền, hàm dùng giá trị mặc định.

```python
def chao(name, loi_chao="Xin chào"):
    print(f"{loi_chao}, {name}!")

chao("Lan")                    # Xin chào, Lan!
chao("Bình", "Chào buổi sáng") # Chào buổi sáng, Bình!
```

Lưu ý: tham số có giá trị mặc định phải đặt **sau** các tham số không có mặc định.

### 1.6. Phạm vi biến (scope)

Biến tạo **bên trong** hàm chỉ tồn tại trong hàm đó (gọi là biến cục bộ). Bên ngoài không thấy được.

```python
def tinh():
    ket_qua = 100          # biến cục bộ, chỉ sống trong hàm tinh()
    print(ket_qua)

tinh()
# print(ket_qua)  # LỖI! ket_qua không tồn tại ở ngoài hàm
```

Biến tạo ngoài hàm gọi là biến toàn cục — hàm có thể **đọc** được:

```python
thue_suat = 0.1            # biến toàn cục

def tinh_thue(gia):
    return gia * thue_suat # đọc được biến toàn cục

print(tinh_thue(1000))     # 100.0
```
