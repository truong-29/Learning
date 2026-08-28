# Bài 07 — Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 07
> Độ khó: Khó (Hard)

Các bài này gần với bài toán thực tế, kết hợp list, tuple, slice, vòng lặp và xử lý trường hợp biên. Nếu bí, xem [gợi ý hướng dẫn](../goi-y/huong-dan.md) (không phải lời giải sẵn).

1. **Bảng xếp hạng điểm thi**: Cho một list các tuple `(ten, diem)`, ví dụ `[("Lan", 8), ("Bình", 6), ("Cường", 9)]`. In danh sách theo thứ tự điểm từ cao xuống thấp, kèm số thứ hạng (1, 2, 3...). Xử lý trường hợp list rỗng thì in "Chưa có dữ liệu".

2. **Gộp và thống kê hai lớp**: Cho hai list điểm của hai lớp. Gộp thành một list, rồi in: tổng số học sinh, điểm trung bình chung (làm tròn 2 chữ số), điểm cao nhất và có bao nhiêu bạn đạt điểm trên trung bình chung. Không dùng `set`, chỉ dùng list và vòng lặp.

3. **Xoay vòng danh sách**: Viết chương trình nhận một list và một số `k`, rồi tạo list mới bằng cách "xoay" list sang phải `k` bước (phần tử cuối chuyển lên đầu). Ví dụ `[1, 2, 3, 4, 5]` xoay 2 bước thành `[4, 5, 1, 2, 3]`. Xử lý trường hợp `k` lớn hơn độ dài list (gợi ý: dùng phép chia lấy dư với `len`).
