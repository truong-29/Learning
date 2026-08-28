# Bài 11 — Xử lý lỗi (try/except) · Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 11
>
> **Độ khó: Trung bình (Medium)**

Các bài này kết hợp hàm, `raise`, vòng lặp nhập lại, và xử lý nhiều loại lỗi cùng lúc.

1. Viết hàm `chia_an_toan(a, b)` trả về kết quả `a / b`, nhưng nếu `b = 0` thì trả về `None` và in cảnh báo. Test hàm với vài cặp số.
2. Viết chương trình yêu cầu người dùng nhập tuổi. Nếu tuổi nhỏ hơn 0 hoặc lớn hơn 150, dùng `raise ValueError` với thông báo phù hợp. Bắt lỗi và cho nhập lại đến khi hợp lệ.
3. Viết hàm đọc file JSON an toàn: nếu file không tồn tại (`FileNotFoundError`) hoặc nội dung không phải JSON hợp lệ (`json.JSONDecodeError`), trả về một dict rỗng thay vì để sập.

---

⬅️ Quay lại [Độ khó Dễ](de.md) · ➡️ Thử thách [Độ khó Khó](kho.md)
