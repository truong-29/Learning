# Bài 05 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 05

## 📖 1. Kiến thức cơ bản

### 1.1. Vòng lặp là gì?

Hãy tưởng tượng bạn phải viết dòng chữ "Tôi sẽ chăm học" 100 lần lên bảng. Viết tay từng dòng thì rất mệt. Vòng lặp giúp máy tính **làm đi làm lại một việc** mà bạn chỉ cần viết một lần.

Trong Python có 2 loại vòng lặp chính: `for` và `while`.

### 1.2. Vòng lặp `for` với `range()`

`for` dùng khi bạn **biết trước** sẽ lặp bao nhiêu lần, hoặc muốn duyệt qua một dãy giá trị.

```python
# In ra các số từ 0 đến 4
for i in range(5):
    print(i)
```

Kết quả in ra (mỗi số một dòng): `0 1 2 3 4`. Lưu ý `range(5)` tạo ra dãy **từ 0 đến 4** (5 số), không bao gồm số 5.

Biến `i` là "biến đếm" — mỗi vòng lặp nó nhận một giá trị mới trong dãy.

### 1.3. Ba cách dùng `range()`

```python
# 1. range(stop): từ 0 đến stop-1
for i in range(3):
    print(i)          # 0, 1, 2

# 2. range(start, stop): từ start đến stop-1
for i in range(2, 6):
    print(i)          # 2, 3, 4, 5

# 3. range(start, stop, step): thêm bước nhảy
for i in range(0, 10, 2):
    print(i)          # 0, 2, 4, 6, 8
```

`step` có thể là số âm để đếm lùi:

```python
for i in range(5, 0, -1):
    print(i)          # 5, 4, 3, 2, 1
```

### 1.4. Duyệt qua một chuỗi hoặc danh sách

`for` không chỉ dùng với `range()`. Nó có thể duyệt qua từng phần tử:

```python
# Duyệt từng ký tự trong chuỗi
for chu_cai in "Python":
    print(chu_cai)     # P, y, t, h, o, n (mỗi ký tự một dòng)

# Duyệt từng phần tử trong danh sách
mon_hoc = ["Toán", "Lý", "Hóa"]
for mon in mon_hoc:
    print("Hôm nay học:", mon)
```

### 1.5. Vòng lặp `while`

`while` dùng khi bạn **chưa biết trước** số lần lặp, chỉ biết điều kiện dừng. Vòng lặp chạy **chừng nào điều kiện còn đúng**.

```python
# Đếm từ 1 đến 5 bằng while
so = 1
while so <= 5:
    print(so)
    so = so + 1        # BẮT BUỘC phải tăng biến, nếu không sẽ lặp vô tận!
```

Rất quan trọng: bên trong `while` phải có câu lệnh làm cho điều kiện **sớm muộn trở thành sai**, nếu không chương trình sẽ chạy mãi không dừng (gọi là "vòng lặp vô tận").

### 1.6. `break` — thoát khỏi vòng lặp ngay lập tức

```python
# Tìm số đầu tiên chia hết cho 7 trong khoảng 1..50
for i in range(1, 51):
    if i % 7 == 0:
        print("Tìm thấy:", i)
        break          # Dừng vòng lặp ngay, không xét tiếp
```

### 1.7. `continue` — bỏ qua vòng hiện tại, sang vòng kế tiếp

```python
# In các số từ 1 đến 10, nhưng bỏ qua số chẵn
for i in range(1, 11):
    if i % 2 == 0:
        continue       # Bỏ qua phần còn lại, quay lại đầu vòng lặp
    print(i)           # Chỉ in số lẻ: 1, 3, 5, 7, 9
```

### 1.8. Vòng lặp lồng nhau

Một vòng lặp có thể nằm bên trong vòng lặp khác. Vòng bên trong chạy **trọn vẹn** cho mỗi lần vòng ngoài chạy.

```python
# In bảng cửu chương từ 2 đến 4
for bang in range(2, 5):          # vòng ngoài: chọn bảng
    print(f"--- Bảng {bang} ---")
    for nhan in range(1, 6):      # vòng trong: nhân từ 1 đến 5
        print(f"{bang} x {nhan} = {bang * nhan}")
```
