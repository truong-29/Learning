# Bài 02 — Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 02
> Độ khó: Khó (Hard)

Các bài này kết hợp biến, bốn kiểu dữ liệu, `type()` và ép kiểu. Dùng biến gán sẵn (chưa cần `input()`). Nếu bí, xem [gợi ý hướng dẫn](../goi-y/huong-dan.md).

1. **Tính diện tích và chi phí sơn phòng.** Cho các biến gán sẵn:

   ```python
   chieu_dai = 5.0          # mét (float)
   chieu_rong = 4.0         # mét (float)
   chieu_cao = 3.0          # mét (float)
   dien_tich_cua_so = 5.5   # m2 phần tường KHÔNG sơn (float)
   gia_moi_m2 = "25000"     # chuỗi (str), đơn vị đồng/m2
   so_nguoi_chia_tien = "2" # chuỗi (str)
   ```

   Thực hiện lần lượt các bước sau:
   1. Tính diện tích bốn bức tường theo công thức `2 * (chieu_dai + chieu_rong) * chieu_cao`, lưu vào một biến.
   2. Tính diện tích cần sơn = diện tích bốn bức tường **trừ** `dien_tich_cua_so`.
   3. `gia_moi_m2` đang là chuỗi — ép nó sang số nguyên, rồi tính tổng chi phí = diện tích cần sơn nhân với giá mỗi m2.
   4. `so_nguoi_chia_tien` cũng là chuỗi — ép sang số nguyên, rồi tính chi phí mỗi người = tổng chi phí chia cho số người.
   5. Dùng `type()` để in ra kiểu của diện tích cần sơn và kiểu của tổng chi phí. Suy nghĩ: vì sao kết quả các phép nhân/chia này lại là `float`?
   6. In ra nhiều dòng thông tin (diện tích bốn bức tường, diện tích cần sơn, tổng chi phí, chi phí mỗi người): dùng dấu phẩy trong `print` để ghép nhãn chữ với số. Thêm **ít nhất một** dòng in ra bằng cách ghép chuỗi với dấu `+` (nhớ ép số sang `str` trước), ví dụ `"Tong chi phi son la: " + ...`.

2. **Kiểm tra và ép kiểu chuỗi số.** Cho `chuoi_a = "3.5"` và `chuoi_b = "10"`. Hãy dùng `type()` in ra kiểu của hai chuỗi này (để thấy chúng là `str`), sau đó ép `chuoi_a` sang `float`, `chuoi_b` sang `int`, tính tổng của hai số vừa ép và in ra kết quả kèm kiểu của tổng đó. Suy nghĩ: tổng sẽ mang kiểu gì, `int` hay `float`? Vì sao?

3. **Chỉ số BMI.** Cho `can_nang = 68` (kg, int) và `chieu_cao = 1.70` (m, float). Tính chỉ số BMI theo công thức `BMI = can_nang / (chieu_cao * chieu_cao)`. In ra một câu hoàn chỉnh dạng chuỗi ghép, ví dụ `Chi so BMI cua ban la: 23.52...`. Cạm bẫy: để ghép số vào câu bằng dấu `+`, bạn phải ép số sang `str` trước; kiểm tra lại kiểu của kết quả phép chia bằng `type()`.
