# Bài 04 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 04

## 📖 1. Kiến thức cơ bản

### 4.1. Vì sao cần câu điều kiện?

Trong đời sống ta luôn ra quyết định: "**Nếu** trời mưa **thì** mang ô". Chương trình cũng vậy — nó cần rẽ nhánh tùy tình huống. Câu lệnh `if` (nghĩa là "nếu") giúp máy tính làm điều đó.

### 4.2. Câu lệnh `if`

Cú pháp: từ khóa `if`, một điều kiện, dấu hai chấm `:`, rồi khối lệnh **thụt vào** bên dưới.

```python
tuoi = 20

if tuoi >= 18:                 # nếu tuoi lớn hơn hoặc bằng 18
    print("Bạn đã đủ tuổi.")   # dòng này thụt vào, chỉ chạy khi điều kiện đúng

print("Kết thúc chương trình.")   # dòng này KHÔNG thụt, luôn chạy
```

Nếu `tuoi` là 20 (đúng ≥ 18), máy in cả hai dòng. Nếu `tuoi` là 15, chỉ in dòng cuối.

### 4.3. Thụt lề (indentation) — cực kỳ quan trọng

Python dùng **khoảng trắng thụt đầu dòng** để biết những lệnh nào thuộc về `if`. Chuẩn là **4 dấu cách** (trong VS Code nhấn phím `Tab` sẽ tự thêm). Các dòng cùng thụt một mức thuộc cùng một khối.

```python
if True:
    print("Dòng 1 trong if")   # thuộc if
    print("Dòng 2 trong if")   # cũng thuộc if (cùng mức thụt)
print("Dòng ngoài if")          # không thuộc if
```

Thụt lề sai sẽ gây lỗi `IndentationError`. Đây là lỗi phổ biến nhất của người mới!

### 4.4. `if ... else` — hai lựa chọn

`else` (nghĩa là "ngược lại") chạy khi điều kiện `if` sai:

```python
diem = 4

if diem >= 5:
    print("Đậu")       # chạy khi diem >= 5
else:
    print("Rớt")       # chạy khi diem < 5

# diem = 4 nên in ra: Rớt
```

### 4.5. `if ... elif ... else` — nhiều nhánh

Khi có nhiều trường hợp, dùng `elif` (viết tắt của "else if" — "ngược lại nếu"). Python kiểm tra lần lượt từ trên xuống, gặp điều kiện đúng đầu tiên thì chạy nhánh đó rồi bỏ qua phần còn lại.

```python
diem = 8

if diem >= 9:
    print("Xuất sắc")
elif diem >= 7:            # nếu chưa >= 9 nhưng >= 7
    print("Khá")
elif diem >= 5:            # nếu chưa >= 7 nhưng >= 5
    print("Trung bình")
else:                     # tất cả trên đều sai
    print("Yếu")

# diem = 8 → in ra: Khá
```

Thứ tự rất quan trọng: vì `8 >= 7` đúng nên in "Khá" và dừng, không xét tiếp.

### 4.6. Kết hợp điều kiện & điều kiện lồng nhau

Dùng `and`, `or`, `not` (đã học ở Bài 03) để ghép điều kiện; hoặc đặt `if` bên trong `if` (gọi là **lồng nhau**):

```python
tuoi = 20
co_ve = True

# Ghép điều kiện bằng and
if tuoi >= 18 and co_ve:
    print("Được vào xem phim người lớn.")

# Điều kiện lồng nhau
if tuoi >= 18:
    if co_ve:
        print("Mời bạn vào.")     # chỉ chạy khi CẢ HAI đúng
    else:
        print("Bạn cần mua vé.")  # đủ tuổi nhưng chưa có vé
else:
    print("Bạn chưa đủ tuổi.")
```
