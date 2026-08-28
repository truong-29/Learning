# Bài 03 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 03

## ⚠️ Lỗi thường gặp

- **Quên ép kiểu sau `input()`:** `tuoi = input(...)` rồi `tuoi + 1` sẽ báo `TypeError` vì `tuoi` là chuỗi. Nhớ `int(...)` hoặc `float(...)`.
- **Nhầm `=` với `==`:** viết `if x = 5` báo `SyntaxError`. So sánh phải dùng `==`.
- **Quên chữ `f` trong f-string:** `print("{ten}")` in ra đúng chữ `{ten}` chứ không phải giá trị. Phải có `f` phía trước: `print(f"{ten}")`.
- **Chia cho 0:** `10 / 0` báo lỗi `ZeroDivisionError`. Đừng chia cho 0.
