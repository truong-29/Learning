# Bài 04 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 04

## ⚠️ Lỗi thường gặp

- **Quên dấu hai chấm `:`** sau điều kiện: `if diem >= 5` (thiếu `:`) gây `SyntaxError`. Luôn có `:` cuối dòng `if`/`elif`/`else`.
- **Thụt lề sai/không đều:** trộn Tab và dấu cách, hoặc quên thụt lề, gây `IndentationError`. Hãy dùng đều 4 dấu cách.
- **Nhầm `=` với `==`:** `if diem = 5:` sai. So sánh phải dùng `==`.
- **`else`/`elif` có điều kiện thừa:** `else` KHÔNG được kèm điều kiện (`else diem < 5:` là sai). `else` đứng một mình, chỉ `elif` mới kèm điều kiện.
