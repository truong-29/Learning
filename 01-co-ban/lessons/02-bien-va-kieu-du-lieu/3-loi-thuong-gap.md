# Bài 02 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 02

## ⚠️ Lỗi thường gặp

- **Cộng chuỗi với số:** `"Tuổi: " + 20` báo lỗi `TypeError`. Không thể cộng str với int. Sửa bằng ép kiểu: `"Tuổi: " + str(20)`, hoặc dùng dấu phẩy: `print("Tuổi:", 20)`.
- **Ép chữ không phải số sang int:** `int("hai mươi")` báo lỗi `ValueError`. `int()` chỉ đổi được chuỗi chứa chữ số như `"20"`.
- **Viết `true`/`false` thường:** Python yêu cầu `True` và `False` viết hoa chữ đầu. Viết thường sẽ báo lỗi `NameError`.
- **Đặt tên biến sai:** dùng dấu cách (`ho ten`) hay bắt đầu bằng số (`1diem`) đều gây `SyntaxError`. Hãy dùng `ho_ten`, `diem1`.
