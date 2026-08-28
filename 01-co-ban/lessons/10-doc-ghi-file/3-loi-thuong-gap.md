# Bài 10 — Đọc/ghi file văn bản · Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 10

## ⚠️ Lỗi thường gặp
- **Dùng `"w"` khi muốn giữ dữ liệu cũ**: chế độ `"w"` xóa sạch nội dung file. Muốn thêm mà không mất dữ liệu, dùng `"a"`.
- **Quên đóng file**: nếu không dùng `with` mà quên `f.close()`, dữ liệu có thể chưa được ghi xuống đĩa. Ưu tiên luôn dùng `with`.
- **Mở file không tồn tại với `"r"`**: gây lỗi `FileNotFoundError`. Kiểm tra tên/đường dẫn file, hoặc xử lý lỗi (học ở Bài 11).
- **Quên `.strip()` khi đọc từng dòng**: mỗi dòng đọc lên còn dính ký tự xuống dòng `\n` ở cuối, làm kết quả in ra bị cách dòng thừa.
- **Lỗi tiếng Việt bị vỡ**: quên `encoding="utf-8"` khiến chữ có dấu hiển thị sai.

---

⬅️ Quay lại [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md) · ➡️ Bắt tay làm [Bài tập](bai-tap/de.md)
