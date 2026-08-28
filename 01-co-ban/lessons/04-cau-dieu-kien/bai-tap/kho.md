# Bài 04 — Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 04
> Độ khó: Khó (Hard)

Các bài này kết hợp `if`/`elif`/`else`, điều kiện lồng nhau, toán tử logic và xử lý trường hợp biên. Nếu bí, xem [gợi ý hướng dẫn](../goi-y/huong-dan.md).

1. **Phân loại tam giác.** Nhập ba cạnh `a`, `b`, `c`. Trước hết kiểm tra ba cạnh có tạo thành tam giác hợp lệ không (mỗi cạnh phải dương VÀ tổng hai cạnh bất kỳ lớn hơn cạnh còn lại). Nếu hợp lệ, phân loại: tam giác đều (ba cạnh bằng nhau), cân (đúng hai cạnh bằng nhau), hay thường. Nếu không hợp lệ, báo "Không phải tam giác". Chú ý xử lý đủ các trường hợp biên.

2. **Tính tiền taxi.** Nhập số km đi được. Biểu giá: 0,5 km đầu giá mở cửa cố định 11000đ; từ sau 0,5 km đến hết 30 km giá 14500đ/km; phần vượt quá 30 km giá 11600đ/km. In ra tổng tiền. Dùng `if`/`elif` để chọn đúng công thức theo quãng đường, cẩn thận ranh giới 0,5 km và 30 km.

3. **Xếp hạng BMI.** Nhập cân nặng (kg) và chiều cao (m). Tính BMI = cân nặng chia cho bình phương chiều cao. Sau đó dùng `if`/`elif`/`else` xếp loại: dưới 18.5 là "Thiếu cân", từ 18.5 đến dưới 25 là "Bình thường", từ 25 đến dưới 30 là "Thừa cân", từ 30 trở lên là "Béo phì". Nhớ kiểm tra dữ liệu vô lý (chiều cao hoặc cân nặng không dương) trước khi tính.
