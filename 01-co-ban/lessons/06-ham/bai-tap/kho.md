# Bài 06 — Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 06
> Độ khó: Khó (Hard)

Các bài này kết hợp nhiều hàm, tham số mặc định, `return` và xử lý trường hợp biên gần với thực tế. Nếu bí, xem [gợi ý hướng dẫn](../goi-y/huong-dan.md) (không phải lời giải sẵn).

1. **Máy tính tiền có giảm giá**: Viết hàm `tinh_tien(don_gia, so_luong, phan_tram_giam=0)` trả về số tiền phải trả sau khi áp dụng phần trăm giảm giá. Sau đó viết hàm `in_hoa_don(ten_hang, don_gia, so_luong, phan_tram_giam=0)` gọi lại `tinh_tien` để in một hóa đơn gọn gàng (tên hàng, đơn giá, số lượng, giảm giá, thành tiền). Xử lý trường hợp biên: số lượng hoặc đơn giá âm thì trả về 0 và báo dữ liệu không hợp lệ.

2. **Kiểm tra mật khẩu mạnh**: Viết hàm `mat_khau_manh(mk)` trả về `True` nếu mật khẩu thỏa tất cả điều kiện: dài ít nhất 8 ký tự, có ít nhất 1 chữ số, có ít nhất 1 chữ cái. Ngược lại trả về `False`. Dùng vòng lặp để kiểm tra từng ký tự. Thử hàm với vài mật khẩu khác nhau và in kết quả.

3. **Dãy Fibonacci bằng hàm**: Viết hàm `fibonacci(n)` trả về **danh sách** `n` số Fibonacci đầu tiên (dãy bắt đầu 0, 1, 1, 2, 3, 5...). Xử lý các trường hợp biên: `n = 0` trả về danh sách rỗng, `n = 1` trả về `[0]`. In thử với `n = 10`.
