# Bài 04 — Gợi ý hướng dẫn (KHÔNG phải lời giải)

> Track: Cơ bản (Beginner) · Module 1 · Bài 04

Dưới đây là hướng dẫn gợi mở để bạn **tự viết** code. Không có lời giải hoàn chỉnh.

### Dễ

1. Có ba khả năng: dương, âm, bằng không → cần ba nhánh `if`/`elif`/`else`. Nhập số và ép kiểu trước. So sánh với 0 bằng `>` và `<`; trường hợp còn lại (`else`) chính là bằng 0.
2. Nhập tuổi, ép `int`. Chỉ có hai khả năng nên dùng `if ... else`. Điều kiện là "lớn hơn hoặc bằng 18".
3. Một số chẵn khi chia 2 dư 0, tức `so % 2 == 0`. Dùng `if ... else`: nhánh đúng in "chẵn", nhánh còn lại in "lẻ". Cạm bẫy: dùng `==` để so sánh, đừng dùng `=`.
4. Giống bài 2 về cấu trúc: hai nhánh, điều kiện là điểm "lớn hơn hoặc bằng 5". Nhớ ép điểm sang số (nên `float`).
5. Ba khả năng: số một lớn hơn, số hai lớn hơn, hoặc bằng nhau → `if`/`elif`/`else`. Cạm bẫy: nhớ nhánh bằng nhau, đừng bỏ sót.

### Trung bình

1. Tìm lớn nhất trong ba số: một cách là dùng `if a >= b and a >= c` để bắt trường hợp `a` lớn nhất, rồi `elif b >= c` cho `b`, còn lại `else` là `c`. Bước logic: mỗi nhánh khẳng định một biến lớn nhất bằng cách so với hai biến kia. Cạm bẫy: dùng `>=` (không phải `>`) để không bị kẹt khi có số bằng nhau.
2. Năm nhuận có hai đường thỏa mãn: "chia hết cho 4 VÀ không chia hết cho 100", HOẶC "chia hết cho 400". "Chia hết" nghĩa là phép chia dư 0 (`% == 0`). Ghép hai cụm `and` bằng `or`, mỗi cụm nên đặt trong ngoặc. Dùng `if ... else` để in kết luận.
3. Phương trình bậc nhất: xét trước `a == 0`. Khi `a == 0`: nếu `b == 0` thì vô số nghiệm, ngược lại vô nghiệm — đây là `if` lồng trong nhánh `a == 0`. Khi `a` khác 0 (`else`): nghiệm là `-b / a`, in ra bằng f-string. Cạm bẫy: chỉ được chia cho `a` khi chắc chắn `a` khác 0, nên phải xử lý `a == 0` trước.

### Khó

1. **Phân loại tam giác.** Chia làm hai tầng. Tầng ngoài: kiểm tra hợp lệ — ba cạnh đều dương VÀ mỗi tổng hai cạnh lớn hơn cạnh còn lại (ba bất đẳng thức ghép bằng `and`). Nếu không hợp lệ thì báo và dừng ở nhánh `else`. Tầng trong (khi hợp lệ): so sánh ba cạnh — cả ba bằng nhau là đều; đúng hai cạnh bằng nhau là cân (kiểm tra `a==b` hoặc `b==c` hoặc `a==c`); còn lại là thường. Bước logic: xét "đều" trước, rồi "cân", rồi `else` là "thường". Cạm bẫy: thứ tự quan trọng — nếu xét "cân" trước "đều" thì tam giác đều cũng lọt vào cân; và nhớ dùng `==` để so sánh.
2. **Tiền taxi.** Đây là bài chọn công thức theo khoảng. Dùng `if`/`elif`/`else` theo quãng đường: nếu quãng đường nằm trong 0,5 km đầu thì chỉ tính giá mở cửa; nếu từ trên 0,5 đến 30 km thì giá mở cửa cộng phần km giữa nhân đơn giá; nếu vượt 30 km thì cộng thêm phần vượt nhân đơn giá cao. Bước logic: xác định từng "chặng" đóng góp bao nhiêu tiền, cộng dồn. Cạm bẫy: phần km ở chặng giữa phải trừ đi 0,5 km đầu; phần vượt phải trừ đi 30 km; xử lý đúng ranh giới bằng dấu so sánh phù hợp (`<=` hay `<`).
3. **Xếp hạng BMI.** Kiểm tra hợp lệ trước: nếu chiều cao hoặc cân nặng không dương thì báo lỗi và không tính (nhánh đầu). Ngược lại, tính BMI = cân nặng chia cho (chiều cao nhân chiều cao) — nhớ đặt ngoặc quanh bình phương chiều cao. Sau đó chuỗi `if`/`elif`/`else` xếp loại theo các mốc 18.5, 25, 30, xét từ thấp lên hoặc từ cao xuống nhất quán. Cạm bẫy: các mốc phải không chồng lấn — dùng "nhỏ hơn" cho ngưỡng trên của mỗi loại để mỗi giá trị chỉ rơi vào đúng một nhánh.
