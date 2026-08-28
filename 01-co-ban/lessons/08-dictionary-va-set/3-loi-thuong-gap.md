# Bài 08 — Lỗi thường gặp

> Track: Cơ bản (Beginner) · Module 1 · Bài 08

## ⚠️ Lỗi thường gặp

- **Truy cập key không tồn tại (`KeyError`)**: `dict["khong_co"]` sẽ báo lỗi. Dùng `dict.get("khong_co")` để an toàn.
- **Nhầm `{}` là set rỗng**: `{}` là dictionary rỗng. Set rỗng phải viết `set()`.
- **Trông đợi set có thứ tự**: set không giữ thứ tự phần tử, đừng dùng khi cần giữ trật tự.
- **Dùng kiểu thay đổi được làm key**: key của dictionary phải là kiểu bất biến (chuỗi, số, tuple), không dùng list làm key được.
