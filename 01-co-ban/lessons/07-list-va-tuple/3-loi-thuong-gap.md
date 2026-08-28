# Bài 07 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 07

## ⚠️ Lỗi thường gặp

- **Chỉ số vượt phạm vi (`IndexError`)**: list có 3 phần tử thì chỉ số hợp lệ là 0, 1, 2. Gọi `list[3]` sẽ báo lỗi.
- **Quên list đếm từ 0**: phần tử đầu tiên là `list[0]`, không phải `list[1]`.
- **Nhầm `append` thêm nhiều phần tử**: `append([1,2])` sẽ thêm cả list làm MỘT phần tử. Muốn nối hai list, dùng `extend` hoặc toán tử `+`.
- **Cố sửa tuple**: tuple không thay đổi được, gán lại phần tử sẽ báo `TypeError`.
