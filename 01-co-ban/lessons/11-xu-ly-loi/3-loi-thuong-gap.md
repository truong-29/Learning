# Bài 11 — Xử lý lỗi (try/except) · Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 11

## ⚠️ Lỗi thường gặp
- **Dùng `except:` trơ trọi bắt mọi lỗi**: viết `except:` không nêu loại lỗi sẽ nuốt luôn cả những lỗi bất ngờ, che giấu bug. Hãy bắt đúng loại lỗi cần xử lý.
- **Bọc quá nhiều code trong một `try`**: khó biết dòng nào gây lỗi. Chỉ nên bọc phần code thực sự có nguy cơ.
- **Bắt lỗi rồi bỏ qua im lặng**: dùng `except: pass` khiến lỗi biến mất mà không ai biết. Ít nhất hãy thông báo hoặc ghi log.
- **Nhầm `else` với `except`**: `else` chạy khi KHÔNG có lỗi, không phải khi có lỗi.

---

⬅️ Quay lại [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md) · ➡️ Bắt tay làm [Bài tập](bai-tap/de.md)
