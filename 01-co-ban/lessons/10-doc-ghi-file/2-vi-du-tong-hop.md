# Bài 10 — Đọc/ghi file văn bản · Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 10

## 💡 Ví dụ minh họa tổng hợp
Sổ ghi chú đơn giản: mỗi lần chạy cho phép thêm 1 ghi chú vào file, rồi in ra toàn bộ ghi chú đã có kèm số thứ tự.

```python
TEN_FILE = "ghichu.txt"

# Bước 1: xin người dùng nhập ghi chú mới
ghi_chu_moi = input("Nhap ghi chu moi: ")

# Bước 2: ghi thêm vào cuối file (chế độ "a") — không mất ghi chú cũ
with open(TEN_FILE, "a", encoding="utf-8") as f:
    f.write(ghi_chu_moi + "\n")   # thêm \n để mỗi ghi chú 1 dòng

# Bước 3: đọc lại toàn bộ và in ra có đánh số
print("\n--- DANH SACH GHI CHU ---")
with open(TEN_FILE, "r", encoding="utf-8") as f:
    for so_thu_tu, dong in enumerate(f, start=1):  # enumerate đánh số từ 1
        print(f"{so_thu_tu}. {dong.strip()}")
```

---

⬅️ Quay lại [Lý thuyết](1-ly-thuyet.md) · ➡️ Tiếp theo: [Lỗi thường gặp](3-loi-thuong-gap.md)
