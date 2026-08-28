# Bài 05 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 05

## 💡 Ví dụ minh họa tổng hợp

Chương trình đoán số: máy nghĩ ra số bí mật, người chơi đoán tới khi đúng.

```python
so_bi_mat = 7          # Số máy "nghĩ" trong đầu
doan = 0               # Số người chơi đoán, khởi tạo khác số bí mật
lan_doan = 0           # Đếm số lần đã đoán

while doan != so_bi_mat:
    doan = int(input("Đoán một số (1-10): "))
    lan_doan = lan_doan + 1

    if doan < so_bi_mat:
        print("Số bí mật lớn hơn!")
    elif doan > so_bi_mat:
        print("Số bí mật nhỏ hơn!")
    else:
        print(f"Chính xác! Bạn đoán đúng sau {lan_doan} lần.")
```

Giải thích:
- Dùng `while` vì ta **không biết trước** người chơi cần bao nhiêu lần mới đoán đúng.
- Điều kiện `doan != so_bi_mat` giữ vòng lặp chạy tới khi đoán trúng.
- Mỗi vòng, ta gợi ý "lớn hơn / nhỏ hơn" và đếm số lần đoán.
