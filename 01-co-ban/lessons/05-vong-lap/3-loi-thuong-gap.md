# Bài 05 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 05

## ⚠️ Lỗi thường gặp

- **Vòng lặp vô tận với `while`**: quên tăng/giảm biến điều kiện (ví dụ quên `so = so + 1`). Chương trình treo mãi. Cách tránh: luôn kiểm tra điều kiện có thể trở thành sai. Nếu lỡ chạy, nhấn `Ctrl + C` để dừng.
- **Nhầm phạm vi của `range()`**: `range(5)` cho ra 0..4 (không có 5). Muốn đến đúng số N, dùng `range(1, N+1)`.
- **Thụt lề (indent) sai**: mọi câu lệnh trong vòng lặp phải thụt vào cùng một mức. Thiếu thụt lề sẽ báo `IndentationError`.
- **Dùng `break`/`continue` ngoài vòng lặp**: hai lệnh này chỉ có tác dụng bên trong `for` hoặc `while`, đặt ngoài sẽ gây lỗi cú pháp.
