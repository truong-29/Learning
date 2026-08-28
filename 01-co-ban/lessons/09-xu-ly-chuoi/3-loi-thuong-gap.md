# Bài 09 — Xử lý chuỗi · Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 09

## ⚠️ Lỗi thường gặp
- **Nhầm index bắt đầu từ 1**: index bắt đầu từ `0`. `s[len(s)]` sẽ báo lỗi `IndexError` vì vượt quá giới hạn — ký tự cuối là `s[len(s)-1]` hoặc `s[-1]`.
- **Quên rằng method trả về chuỗi mới**: viết `s.upper()` mà không gán lại thì `s` không đổi. Phải viết `s = s.upper()`.
- **Cố sửa 1 ký tự**: `s[0] = "A"` gây `TypeError` vì chuỗi bất biến. Hãy tạo chuỗi mới bằng slice hoặc `replace`.
- **Cộng chuỗi với số**: `"Tuoi: " + 20` báo `TypeError`. Phải ép kiểu `str(20)` hoặc dùng f-string `f"Tuoi: {20}"`.

---

⬅️ Quay lại [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md) · ➡️ Bắt tay làm [Bài tập](bai-tap/de.md)
