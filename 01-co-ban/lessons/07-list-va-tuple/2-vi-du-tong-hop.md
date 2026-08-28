# Bài 07 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 07

## 💡 Ví dụ minh họa tổng hợp

Chương trình quản lý danh sách việc cần làm:

```python
viec_can_lam = []              # bắt đầu với list rỗng

# Thêm vài việc
viec_can_lam.append("Học Python")
viec_can_lam.append("Tập thể dục")
viec_can_lam.append("Đọc sách")

print("Danh sách việc cần làm:")
# enumerate cho ta cả số thứ tự và giá trị
for so_thu_tu, viec in enumerate(viec_can_lam, start=1):
    print(f"{so_thu_tu}. {viec}")

# Hoàn thành việc đầu tiên -> xóa khỏi list
da_xong = viec_can_lam.pop(0)
print(f"\nĐã hoàn thành: {da_xong}")
print(f"Còn lại {len(viec_can_lam)} việc.")
```

Giải thích:
- Bắt đầu bằng list rỗng rồi `append` từng việc.
- `enumerate(..., start=1)` giúp đánh số thứ tự từ 1 khi in.
- `pop(0)` lấy và xóa việc ở vị trí đầu, `len()` đếm số việc còn lại.
