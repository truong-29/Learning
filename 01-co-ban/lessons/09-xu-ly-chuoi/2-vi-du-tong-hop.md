# Bài 09 — Xử lý chuỗi · Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 09

## 💡 Ví dụ minh họa tổng hợp
Chương trình chuẩn hóa họ tên người dùng nhập (loại khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ) và tách ra họ + tên:

```python
# Người dùng thường gõ lộn xộn, có khoảng trắng thừa
ho_ten_tho = "   nguyen   van AN   "

# Bước 1: bỏ khoảng trắng 2 đầu và viết hoa chữ cái đầu mỗi từ
ho_ten = ho_ten_tho.strip().title()
print(f"Sau chuan hoa: '{ho_ten}'")   # 'Nguyen   Van An' (vẫn còn khoảng trắng giữa)

# Bước 2: split() không tham số sẽ tự gộp các khoảng trắng thừa
cac_tu = ho_ten.split()                # ['Nguyen', 'Van', 'An']
ho_ten_sach = " ".join(cac_tu)         # ghép lại bằng đúng 1 khoảng trắng
print(f"Ket qua: '{ho_ten_sach}'")     # 'Nguyen Van An'

# Bước 3: tách tên (từ cuối) và họ (phần còn lại)
ten = cac_tu[-1]                       # 'An'
ho = " ".join(cac_tu[:-1])             # 'Nguyen Van'
print(f"Ho: {ho}")
print(f"Ten: {ten}")
```

---

⬅️ Quay lại [Lý thuyết](1-ly-thuyet.md) · ➡️ Tiếp theo: [Lỗi thường gặp](3-loi-thuong-gap.md)
