# Bài 10 — Đọc/ghi file văn bản · Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 10
>
> **Độ khó: Khó (Hard)**

Các bài này gần với ứng dụng thật: dữ liệu bền vững qua nhiều lần chạy, thống kê, và xử lý file có thể chưa tồn tại. Vạch các bước rõ ràng trước khi code.

1. **Bộ đếm lượt chạy chương trình.** Mỗi lần chạy, chương trình đọc số lần đã chạy từ file `dem.txt` (nếu file chưa có thì coi như 0), tăng thêm 1, in ra "Đây là lần chạy thứ N", rồi ghi số mới trở lại file. Chạy 3 lần liên tiếp phải in ra 1, 2, 3.

2. **Thống kê tần suất từ trong một đoạn văn.** Đọc file văn bản (nhiều dòng), chuẩn hóa về chữ thường, tách thành các từ, đếm mỗi từ xuất hiện bao nhiêu lần, rồi in ra 3 từ xuất hiện nhiều nhất kèm số lần (sắp xếp giảm dần). Chuẩn bị sẵn một file mẫu vài dòng để thử.

3. **Nhật ký công việc bằng JSON tích lũy.** Xây một chương trình cho phép thêm một công việc mới gồm `tieu_de` và `uu_tien` (cao/thấp) vào file `cong_viec.json`. Mỗi lần chạy: đọc danh sách hiện có (nếu file chưa tồn tại thì bắt đầu bằng list rỗng), thêm công việc mới, lưu lại, rồi in ra toàn bộ danh sách được nhóm theo mức ưu tiên (in nhóm "cao" trước, "thấp" sau).

---

⬅️ Quay lại [Độ khó Trung bình](trung-binh.md) · 💡 Bí thì xem [gợi ý hướng dẫn](../goi-y/huong-dan.md)
