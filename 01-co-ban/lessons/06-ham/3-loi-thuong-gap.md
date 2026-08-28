# Bài 06 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 06

## ⚠️ Lỗi thường gặp

- **Định nghĩa hàm nhưng quên gọi**: viết `def chao():` mà không có dòng `chao()` thì hàm không bao giờ chạy.
- **Nhầm `print` với `return`**: hàm chỉ `print` sẽ hiển thị nhưng trả về `None`, nên `x = ham()` sẽ cho `x = None`. Cần dùng `return` khi muốn tái sử dụng kết quả.
- **Sai số lượng tham số**: định nghĩa `def cong(a, b)` mà gọi `cong(3)` sẽ báo lỗi thiếu tham số.
- **Truy cập biến cục bộ từ bên ngoài**: biến tạo trong hàm không dùng được ở ngoài, sẽ báo `NameError`.
