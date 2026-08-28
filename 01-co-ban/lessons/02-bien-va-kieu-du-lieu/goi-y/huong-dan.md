# Bài 02 — Gợi ý hướng dẫn (KHÔNG phải lời giải)

> Track: Cơ bản (Beginner) · Module 1 · Bài 02

Dưới đây là hướng dẫn gợi mở để bạn **tự viết** code. Không có lời giải hoàn chỉnh — hãy hiểu ý tưởng rồi tự gõ.

### Dễ

1. Tạo ba biến với tên gợi ý trong đề, chú ý `chieu_cao` là số thực nên viết có dấu chấm (ví dụ `1.72`). In cả ba: có thể dùng một `print` với các giá trị cách nhau bằng dấu phẩy, hoặc ba lệnh `print` riêng.
2. Gọi hàm `type()` bọc quanh từng giá trị và đưa vào `print`. Cạm bẫy: `"Python"` phải để trong nháy (là chuỗi), còn `False` viết hoa chữ F (là bool), đừng để trong nháy.
3. Biến `so_chu` đang là chuỗi. Muốn cộng số học phải ép sang `int` trước bằng `int(...)`, sau đó mới cộng `8`. Nếu cộng trực tiếp chuỗi với số sẽ báo lỗi kiểu.
4. `diem` là số nguyên. Để ghép nó vào câu bằng dấu `+`, phải đổi sang chuỗi bằng `str(...)` rồi mới nối với phần chữ. Cách khác đơn giản hơn: dùng dấu phẩy trong `print` để khỏi ép kiểu.
5. Tạo `a` và `b`, rồi in ba biểu thức: `a + b`, `a - b`, `a * b`. Nên kèm nhãn chữ (ví dụ `"Tổng:"`) trước mỗi giá trị cho dễ đọc.

### Trung bình

1. `gia` đang là chuỗi `"150000"`. Ép sang số (dùng `int(...)` hoặc `float(...)`). Giảm 10% nghĩa là còn lại 90%, tức nhân với `0.9`. In kết quả kèm nhãn chữ. Cạm bẫy: nếu nhân với `0.9` kết quả sẽ là số thực (`float`), nên phần thập phân `.0` xuất hiện là bình thường.
2. Thay trực tiếp công thức `C * 9 / 5 + 32` vào code với biến `nhiet_do_c`. Lưu ý thứ tự phép tính: nhân/chia làm trước cộng. In cả nhiệt độ C ban đầu lẫn nhiệt độ F vừa tính, dùng dấu phẩy trong `print` để ghép chữ và số.
3. Bí quyết hoán đổi trong Python nằm ngay ở gợi ý đề: một dòng `x, y = y, x` sẽ tráo hai giá trị cùng lúc. Sau đó in `x` và `y` để kiểm chứng. Cạm bẫy nếu tự nghĩ cách khác: gán `x = y` trước sẽ làm mất giá trị cũ của `x`, nên cần biến tạm — nhưng cách một dòng ở trên tránh được điều đó.

### Khó

1. **Tính diện tích và chi phí sơn phòng.** Đây là bài nhiều bước — làm tuần tự và lưu mỗi kết quả trung gian vào một biến riêng, đừng dồn tất cả vào một dòng. Bước tính tường: nhớ đặt dấu ngoặc quanh `chieu_dai + chieu_rong` rồi mới nhân với `2` và với `chieu_cao`, nếu thiếu ngoặc thứ tự phép tính sẽ sai. Diện tích cần sơn chỉ là phép trừ diện tích tường cho phần cửa sổ. Với `gia_moi_m2` và `so_nguoi_chia_tien`: chúng là chuỗi, phải ép sang số bằng `int(...)` trước khi đưa vào phép nhân/chia — cộng/nhân trực tiếp chuỗi với số sẽ báo lỗi kiểu. Về câu hỏi kiểu: một khi có `float` tham gia phép nhân, hoặc dùng phép chia `/`, Python cho ra `float`; tự kiểm chứng bằng `type(...)` bọc quanh biến kết quả. Khi in: dùng dấu phẩy để `print` tự chèn khoảng trắng giữa nhãn chữ và số cho gọn; còn dòng ghép bằng dấu `+` thì mọi thành phần phải cùng là chuỗi, nên bọc `str(...)` quanh con số. Cạm bẫy: đừng quên dùng "diện tích cần sơn" (đã trừ cửa sổ) khi tính chi phí, không phải diện tích tường ban đầu.
2. **Kiểm tra và ép kiểu.** Trước tiên gọi `type(chuoi_a)` và `type(chuoi_b)` để xác nhận là `str`. Sau đó ép: `float(chuoi_a)` và `int(chuoi_b)`. Cộng hai số đã ép. Về câu hỏi kiểu của tổng: khi cộng một `float` với một `int`, Python nâng kết quả lên `float`. Hãy tự kiểm chứng bằng `type(...)` bọc quanh tổng. Cạm bẫy: đừng ép `chuoi_a` sang `int` vì chuỗi `"3.5"` có dấu chấm sẽ gây lỗi giá trị.
3. **BMI.** Đặt công thức `can_nang / (chieu_cao * chieu_cao)` vào một biến. Phép chia `/` luôn cho `float`, nên BMI là số thực. Để in thành một câu bằng dấu `+`, ép BMI sang chuỗi bằng `str(...)` rồi nối với phần chữ; hoặc dùng dấu phẩy trong `print` để khỏi ép. Cạm bẫy: nhớ đặt dấu ngoặc quanh `chieu_cao * chieu_cao`, nếu không thứ tự phép tính sẽ sai.
