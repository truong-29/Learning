# Bài 08 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 08

## 💡 Ví dụ minh họa tổng hợp

Chương trình đếm số lần xuất hiện của mỗi từ trong câu:

```python
cau = "táo cam táo chuối cam táo"

# Tách câu thành list các từ
danh_sach_tu = cau.split()     # ['táo', 'cam', 'táo', ...]

# Dùng dictionary để đếm
dem = {}
for tu in danh_sach_tu:
    if tu in dem:
        dem[tu] = dem[tu] + 1  # đã có -> tăng thêm 1
    else:
        dem[tu] = 1            # lần đầu gặp -> đặt là 1

# In kết quả
for tu, so_lan in dem.items():
    print(f"'{tu}' xuất hiện {so_lan} lần")
```

Giải thích:
- `split()` cắt câu thành list các từ dựa vào khoảng trắng.
- Dùng dictionary với key là từ, value là số lần xuất hiện.
- Với mỗi từ: nếu đã có trong dict thì tăng đếm, chưa có thì khởi tạo bằng 1.
- Kết quả: táo 3, cam 2, chuối 1.
