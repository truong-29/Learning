# Bài 10 — Đọc/ghi file văn bản · Lý thuyết

> Track: Cơ bản (Beginner) · Module 1 · Bài 10

## 📖 1. Kiến thức cơ bản

### 1.1. Vì sao cần đọc/ghi file?
Khi chương trình chạy, mọi biến nằm trong bộ nhớ (RAM). Tắt chương trình là **mất sạch**. Để giữ dữ liệu lâu dài — như danh sách chi tiêu, ghi chú, điểm số — ta phải **lưu ra file** trên ổ đĩa. Lần sau mở lại, đọc file để lấy dữ liệu về.

Hãy tưởng tượng: RAM giống như trí nhớ ngắn hạn (quên nhanh), còn file giống như quyển sổ tay (ghi lại để đọc sau).

### 1.2. Mở file với `open()`
Hàm `open()` cần 2 thông tin: tên file và **chế độ** mở.

```python
# open(tên_file, chế_độ, encoding)
f = open("ghichu.txt", "w", encoding="utf-8")  # mở để GHI
f.write("Xin chao!")   # ghi nội dung vào file
f.close()              # BẮT BUỘC đóng file sau khi dùng xong
```

> `encoding="utf-8"` giúp lưu và đọc đúng tiếng Việt có dấu. Luôn nên thêm tham số này.

### 1.3. Dùng `with` — cách được khuyên dùng
Nếu quên `f.close()`, file có thể bị lỗi hoặc mất dữ liệu. Khối `with` sẽ **tự động đóng file** khi xong, kể cả khi có lỗi xảy ra.

```python
# Cách tốt nhất: dùng with, không cần gọi close()
with open("ghichu.txt", "w", encoding="utf-8") as f:
    f.write("Xin chao Python!")
# Ra khỏi khối with là file tự đóng — an toàn và gọn gàng
```

### 1.4. Các chế độ mở file
| Chế độ | Ý nghĩa | Nếu file chưa tồn tại | Dữ liệu cũ |
|--------|---------|------------------------|------------|
| `"r"`  | Đọc (read) | Báo lỗi | Giữ nguyên |
| `"w"`  | Ghi (write) | Tạo mới | **Xóa sạch, ghi đè** |
| `"a"`  | Ghi thêm (append) | Tạo mới | Giữ nguyên, viết nối vào cuối |

```python
# "w" — ghi đè: mỗi lần chạy sẽ xóa nội dung cũ
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Dong 1\n")   # \n là ký tự xuống dòng

# "a" — ghi thêm: nối vào cuối, KHÔNG xóa nội dung cũ
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Dong 2\n")
```

### 1.5. Đọc file
Có 3 cách đọc thông dụng:

```python
# Cách 1: read() — đọc TOÀN BỘ file thành 1 chuỗi
with open("log.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
    print(noi_dung)

# Cách 2: readlines() — đọc thành LIST, mỗi dòng là 1 phần tử
with open("log.txt", "r", encoding="utf-8") as f:
    cac_dong = f.readlines()   # ['Dong 1\n', 'Dong 2\n']
    print(cac_dong)

# Cách 3: lặp trực tiếp qua file — tiết kiệm bộ nhớ, hay dùng nhất
with open("log.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print(dong.strip())    # strip() bỏ ký tự xuống dòng \n ở cuối
```

### 1.6. Làm việc với JSON
JSON là định dạng văn bản để lưu dữ liệu có cấu trúc (list, dict). Nó rất phổ biến khi lưu cấu hình, dữ liệu ứng dụng. Python có sẵn module `json`.

```python
import json

# Ghi dữ liệu (dict/list) ra file JSON
du_lieu = {"ten": "An", "tuoi": 20, "mon_hoc": ["Python", "SQL"]}
with open("data.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False để giữ tiếng Việt, indent=2 để dễ đọc
    json.dump(du_lieu, f, ensure_ascii=False, indent=2)

# Đọc dữ liệu JSON từ file, trả về lại dict/list
with open("data.json", "r", encoding="utf-8") as f:
    du_lieu_doc = json.load(f)
    print(du_lieu_doc["ten"])       # An
    print(du_lieu_doc["mon_hoc"])   # ['Python', 'SQL']
```

> Ghi nhớ: `json.dump` (ghi ra **file**), `json.load` (đọc từ **file**). (Còn `json.dumps`/`json.loads` có chữ `s` là làm việc với **chuỗi** — sẽ gặp sau.)

---

⬅️ Quay lại [Mục lục bài](README.md) · ➡️ Tiếp theo: [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md)
