# Bài 11 — Xử lý lỗi (try/except) · Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 11
>
> **Độ khó: Khó (Hard)**

Các bài này gần với chương trình thực tế: nhập liệu bền bỉ, kết hợp nhiều loại lỗi, và giữ cho ứng dụng không bao giờ "sập". Vạch các bước rõ ràng trước khi code.

1. **Máy tính bỏ túi chống sập.** Viết vòng lặp cho phép người dùng nhập hai số và một phép toán (`+ - * /`). Chương trình phải xử lý mọi tình huống sai: nhập chữ thay vì số (`ValueError`), chia cho 0 (`ZeroDivisionError`), và phép toán không hợp lệ (tự `raise ValueError`). Sau mỗi phép tính hỏi người dùng có tiếp tục không; dùng `finally` để in một dòng ngăn cách sau mỗi lượt.

2. **Nhập điểm hợp lệ vào danh sách.** Cho phép người dùng nhập lần lượt điểm của nhiều môn (nhập chữ `xong` để dừng). Mỗi điểm phải là số từ 0 đến 10; nếu ngoài khoảng thì `raise ValueError` với thông báo rõ ràng và cho nhập lại môn đó. Cuối cùng in điểm trung bình. Phải xử lý được cả trường hợp người dùng không nhập điểm nào (tránh chia cho 0 khi tính trung bình).

3. **Đọc cấu hình JSON với giá trị mặc định.** Viết hàm `doc_cau_hinh(ten_file)` đọc một file JSON chứa dict cấu hình. Nếu file không tồn tại, JSON hỏng, hoặc thiếu một key bắt buộc (ví dụ `"ten_ung_dung"`), hàm phải trả về một cấu hình mặc định hợp lý thay vì để sập, đồng thời in cảnh báo cho biết đã dùng giá trị mặc định vì lý do gì (phân biệt được ba nguyên nhân: không có file, JSON lỗi, thiếu key).

---

⬅️ Quay lại [Độ khó Trung bình](trung-binh.md) · 💡 Bí thì xem [gợi ý hướng dẫn](../goi-y/huong-dan.md)
