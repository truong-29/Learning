# Bài 03 — Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 03
> Độ khó: Khó (Hard)

Các bài này kết hợp toán tử số học, so sánh, logic, `input()` và f-string vào những tình huống gần thực tế. Nếu bí, xem [gợi ý hướng dẫn](../goi-y/huong-dan.md).

1. **Máy tính tiền điện.** Nhập số điện tiêu thụ (kWh). Tính tiền theo bậc thang: 50 kWh đầu giá 1700đ/kWh, phần vượt quá 50 kWh giá 2000đ/kWh. In ra tổng tiền bằng f-string. (Chưa dùng `if` — hãy suy nghĩ cách tính phần vượt bằng phép trừ và tận dụng việc phần vượt có thể âm... hoặc thử với số nhập luôn lớn hơn 50 trước, rồi mở rộng sau khi học Bài 04.)

2. **Đổi tiền lẻ trả lại.** Một món hàng giá `X` đồng, khách đưa `Y` đồng. Nhập `X` và `Y`. In ra số tiền phải trả lại và tách số tiền trả lại đó thành số tờ 50000, 20000, 10000, 5000 và phần lẻ còn lại, dùng `//` và `%`. In gọn bằng f-string.

3. **Kiểm tra "giờ hành chính".** Nhập một giờ trong ngày dưới dạng số nguyên 0–23. Dùng toán tử so sánh và logic `and` để in ra `True` nếu giờ đó nằm trong khoảng làm việc (từ 8 đến 11 hoặc từ 13 đến 17), ngược lại `False`. Gợi ý: ghép hai khoảng bằng `or`, mỗi khoảng ghép hai điều kiện bằng `and`.
