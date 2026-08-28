# Bài 03 — Gợi ý hướng dẫn (KHÔNG phải lời giải)

> Track: Cơ bản (Beginner) · Module 1 · Bài 03

Dưới đây là hướng dẫn gợi mở để bạn **tự viết** code. Không có lời giải hoàn chỉnh.

### Dễ

1. Nhận số bằng `input(...)` rồi ép sang số (dùng `float(...)` để nhận cả số lẻ). Bình phương là số nhân chính nó, có thể tính ngay trong dấu `{}` của f-string. Cạm bẫy: quên ép kiểu thì phép nhân trên chuỗi sẽ cho kết quả sai (lặp chuỗi).
2. Nhập tên (giữ nguyên chuỗi) và tuổi (ép sang `int` vì cần cộng 1). Dùng một f-string có hai chỗ `{}`: một cho tên, một cho biểu thức `tuoi + 1`. Cạm bẫy: nếu không ép tuổi sang số, `tuoi + 1` sẽ báo lỗi kiểu.
3. Nhập hai số, ép sang số. In ba dòng cho ba phép: `/`, `//`, `%`. Nhớ khác biệt: `/` cho số thực, `//` bỏ phần lẻ, `%` cho số dư. Cạm bẫy: nếu số thứ hai là 0 sẽ lỗi chia cho 0.
4. Nhập một số, ép kiểu, rồi đặt biểu thức so sánh `so > 100` vào `{}` của f-string. Kết quả của biểu thức so sánh là `True`/`False` nên in thẳng ra được.
5. Nhập giá (nên ép `float`) và số lượng (nên ép `int`). Tổng tiền là tích của hai biến, đặt ngay trong `{}` của f-string. Kèm đơn vị tiền cho rõ.

### Trung bình

1. Đổi giây sang giờ/phút/giây là bài toán chia bậc. Số giờ = tổng giây chia nguyên cho 3600. Phần còn lại = tổng giây chia dư cho 3600. Từ phần còn lại đó: số phút = chia nguyên cho 60, số giây = chia dư cho 60. Bước logic: tính lần lượt và luôn dùng "phần còn lại" của bước trước. Cạm bẫy: đừng lấy tổng giây gốc để tính phút, phải lấy phần dư sau khi trừ giờ.
2. Nhập chiều dài, chiều rộng (ép số). Chu vi = 2 nhân tổng hai cạnh; diện tích = tích hai cạnh. In hai kết quả bằng f-string. Cạm bẫy: nhớ dấu ngoặc quanh tổng hai cạnh khi nhân 2.
3. Nhập tuổi (ép `int`). Điều kiện đủ lái xe là "lớn hơn hoặc bằng 18" VÀ "nhỏ hơn 65", ghép bằng `and`. Gán kết quả biểu thức vào một biến rồi in, hoặc in thẳng biểu thức trong f-string. Kết quả là `True`/`False`.

### Khó

1. **Tiền điện bậc thang.** Ý tưởng: phần dùng ở bậc 1 nhiều nhất là 50 kWh; phần vượt là "tổng kWh trừ 50". Tính tiền = (kWh bậc 1) × 1700 + (kWh vượt) × 2000. Với kiến thức hiện tại (chưa có `if`), hãy thử trước với số nhập chắc chắn lớn hơn 50, tính phần vượt bằng phép trừ. Bước logic: tách phần vượt, nhân đơn giá từng bậc, cộng lại, in bằng f-string. Cạm bẫy: nếu người dùng nhập dưới 50 thì phần vượt ra số âm và kết quả sai — hãy ghi chú điều này và quay lại hoàn thiện sau khi học Bài 04 (dùng `if`).
2. **Trả lại tiền lẻ.** Tiền trả lại = số khách đưa trừ giá món hàng. Sau đó tách số tiền trả lại thành các tờ bằng kỹ thuật chia bậc: số tờ 50000 = chia nguyên cho 50000, phần còn lại = chia dư cho 50000; lặp lại với 20000, 10000, 5000; phần cuối nhỏ hơn 5000 là lẻ. In tất cả bằng f-string. Cạm bẫy: luôn dùng phần còn lại của bước trước, và nhớ ép các số nhập sang `int`.
3. **Giờ hành chính.** Nhập giờ, ép `int`. Buổi sáng: giờ "lớn hơn hoặc bằng 8" `and` "nhỏ hơn hoặc bằng 11". Buổi chiều: giờ "lớn hơn hoặc bằng 13" `and` "nhỏ hơn hoặc bằng 17". Ghép hai buổi bằng `or`. Cạm bẫy: cần đặt dấu ngoặc quanh mỗi cụm `and` trước khi nối bằng `or` để logic rõ ràng và đúng thứ tự.
