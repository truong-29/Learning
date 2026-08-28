# Bài 12 — OOP cơ bản (class, object) · Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 12

## ⚠️ Lỗi thường gặp
- **Quên `self`**: định nghĩa method mà quên tham số `self` đầu tiên sẽ gây `TypeError`. Mọi method đều bắt đầu bằng `self`.
- **Quên `self.` khi truy cập thuộc tính**: viết `ten` thay vì `self.ten` bên trong method sẽ báo lỗi biến chưa định nghĩa.
- **Nhầm class với object**: `ChoCon` là khuôn mẫu, `milu = ChoCon("Milu", 3)` mới là object dùng được. Gọi `ChoCon.sua()` trực tiếp sẽ lỗi vì thiếu object.
- **Hai dấu gạch dưới ở `__init__`**: viết đúng là `__init__` (hai gạch dưới mỗi bên), viết sai thành `_init_` thì hàm khởi tạo không chạy.

---

⬅️ Quay lại [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md) · ➡️ Bắt tay làm [Bài tập](bai-tap/de.md)
