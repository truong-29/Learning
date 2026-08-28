# Bài 11 — Xử lý lỗi (try/except) · Lý thuyết

> Track: Cơ bản (Beginner) · Module 1 · Bài 11

## 📖 1. Kiến thức cơ bản

### 1.1. Lỗi là gì?
Khi chương trình gặp tình huống không xử lý được (chia cho 0, đổi chữ "abc" thành số, mở file không tồn tại...), Python sẽ **ném ra một lỗi (exception)** và **dừng chương trình ngay lập tức**.

```python
tuoi = int("hai muoi")   # ValueError: không đổi được chữ thành số
print("Dong nay khong bao gio chay")   # chương trình đã dừng ở dòng trên
```

Việc "sập" như vậy khiến trải nghiệm rất tệ. Ta cần cách để **bắt lỗi** và xử lý êm đẹp.

### 1.2. try / except — bắt lỗi
Đặt code có thể lỗi vào khối `try`. Nếu lỗi xảy ra, Python nhảy sang khối `except` thay vì sập.

```python
try:
    so = int(input("Nhap mot so: "))   # nếu người dùng gõ chữ → lỗi
    print(f"Binh phuong la {so ** 2}")
except ValueError:
    # Chỉ chạy khi có lỗi ValueError ở khối try
    print("Ban phai nhap MOT SO, khong phai chu!")

print("Chuong trinh van tiep tuc chay binh thuong")
```

Bạn có thể lấy thông tin chi tiết của lỗi bằng `as e`:

```python
try:
    ket_qua = 10 / 0
except ZeroDivisionError as e:
    print(f"Loi xay ra: {e}")   # Loi xay ra: division by zero
```

### 1.3. Bắt nhiều loại lỗi
Một khối `try` có thể có nhiều `except` cho từng loại lỗi khác nhau:

```python
try:
    a = int(input("So thu nhat: "))
    b = int(input("So thu hai: "))
    print(a / b)
except ValueError:
    print("Ban nhap khong phai so!")     # lỗi khi ép kiểu
except ZeroDivisionError:
    print("Khong the chia cho 0!")       # lỗi khi b = 0
```

### 1.4. else và finally
- `else`: chạy khi khối `try` **không** có lỗi.
- `finally`: **luôn luôn** chạy dù có lỗi hay không (thường dùng để dọn dẹp, đóng tài nguyên).

```python
try:
    so = int(input("Nhap so: "))
except ValueError:
    print("Khong hop le!")
else:
    print(f"Ban vua nhap so {so}")   # chỉ chạy khi KHÔNG lỗi
finally:
    print("Cam on ban da su dung chuong trinh")  # LUÔN chạy
```

### 1.5. Các loại lỗi phổ biến
| Loại lỗi | Xảy ra khi |
|----------|-----------|
| `ValueError` | Đổi kiểu dữ liệu không hợp lệ, ví dụ `int("abc")` |
| `ZeroDivisionError` | Chia một số cho 0 |
| `FileNotFoundError` | Mở file không tồn tại với chế độ `"r"` |
| `KeyError` | Truy cập key không có trong dict |
| `IndexError` | Truy cập index vượt ngoài list/chuỗi |
| `TypeError` | Thao tác sai kiểu, ví dụ `"a" + 1` |

```python
diem = {"An": 8, "Binh": 9}
try:
    print(diem["Chi"])         # 'Chi' không tồn tại
except KeyError:
    print("Khong tim thay hoc sinh nay")
```

### 1.6. raise — chủ động ném lỗi
Khi dữ liệu không hợp lệ theo quy tắc của bạn, hãy chủ động phát sinh lỗi bằng `raise`. Điều này giúp phát hiện sai sót sớm thay vì để lỗi mơ hồ xảy ra sau đó.

```python
def dat_tuoi(tuoi):
    if tuoi < 0:
        # Tự ném lỗi với thông báo rõ ràng
        raise ValueError("Tuoi khong the la so am")
    print(f"Tuoi hop le: {tuoi}")

try:
    dat_tuoi(-5)
except ValueError as e:
    print(f"Loi: {e}")   # Loi: Tuoi khong the la so am
```

---

⬅️ Quay lại [Mục lục bài](README.md) · ➡️ Tiếp theo: [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md)
