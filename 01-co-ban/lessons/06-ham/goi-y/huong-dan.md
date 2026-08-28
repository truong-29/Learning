# Bài 06 — Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 06

Trang này **không cho lời giải sẵn**. Mỗi bài chỉ gợi mở hướng đi, các bước logic và cạm bẫy cần tránh để bạn **tự viết** code.

## Dễ

**Bài 1 — `chao_ten(ten)`**
- Định nghĩa hàm nhận một tham số `ten`, bên trong dùng `print` với f-string.
- Nhớ hàm chỉ chạy khi bạn **gọi** nó: viết hai dòng gọi hàm với hai tên khác nhau ở ngoài (không thụt lề).

**Bài 2 — `binh_phuong(x)`**
- Đây là hàm cần **trả về** giá trị, nên dùng `return x * x` chứ không phải `print`.
- Muốn xem kết quả thì bọc lời gọi hàm trong `print(binh_phuong(6))`.

**Bài 3 — `lon_hon(a, b)`**
- Dùng `if` để so sánh. Nếu `a > b` thì `return a`, ngược lại `return b`.
- Nhớ: khi gặp `return`, hàm dừng ngay, nên không cần `else` cũng được.

**Bài 4 — `tinh_tong(a, b, c=0)`**
- Tham số `c` có giá trị mặc định 0 nên khi gọi thiếu `c`, Python tự dùng 0.
- Cạm bẫy: tham số có mặc định phải nằm sau tham số không mặc định (thứ tự `a, b, c=0` là đúng).

**Bài 5 — `dien_tich_hcn(dai, rong)`**
- Diện tích = dài nhân rộng. Dùng `return`, rồi in kết quả khi gọi hàm.

## Trung bình

**Bài 1 — `la_so_nguyen_to(n)`**
- Hàm trả về kiểu bool (`True`/`False`), không in bên trong.
- Xử lý biên: `n < 2` thì `return False` ngay.
- Thử chia `n` cho các số từ 2 tới `n-1`; nếu chia hết thì `return False` luôn (thoát sớm). Nếu vòng lặp chạy hết mà không chia hết lần nào thì `return True`.
- Sau khi có hàm, lặp qua 1..30 và chỉ in số nào khiến hàm trả về `True`.

**Bài 2 — `giai_thua(n)`**
- Bên trong hàm cần biến tích lũy khởi tạo bằng 1, rồi nhân dồn qua vòng lặp từ 1 tới `n`.
- Cạm bẫy `range`: cần `range(1, n+1)` để lấy cả `n`.
- Cuối hàm `return` biến tích lũy.

**Bài 3 — `dem_nguyen_am(chuoi)`**
- Chuẩn bị một biến đếm bằng 0.
- Duyệt từng ký tự trong chuỗi; nếu ký tự nằm trong tập nguyên âm thì tăng đếm.
- Mẹo: có thể kiểm tra nhanh bằng `ky_tu in "aeiou"`. Muốn không phân biệt hoa/thường thì đổi ký tự về chữ thường trước (ví dụ dùng `.lower()`).
- Cuối hàm `return` biến đếm.

## Khó

**Bài 1 — Máy tính tiền có giảm giá**
- `tinh_tien` nên kiểm tra dữ liệu trước tiên: nếu `don_gia < 0` hoặc `so_luong < 0` thì `return 0` (kèm một `print` cảnh báo nếu muốn).
- Công thức: thành tiền gốc = đơn giá × số lượng; số tiền giảm = thành tiền gốc × phần trăm / 100; kết quả = gốc − giảm.
- `in_hoa_don` **không tự tính lại** mà gọi `tinh_tien(...)` để lấy thành tiền, rồi in các dòng thông tin. Đây là cách tái sử dụng hàm.
- Cạm bẫy: phần trăm nhập dạng số như 10 nghĩa là 10%, nhớ chia cho 100.

**Bài 2 — Kiểm tra mật khẩu mạnh**
- Trước vòng lặp, chuẩn bị hai biến cờ: "đã thấy chữ số" và "đã thấy chữ cái", ban đầu đều `False`.
- Duyệt từng ký tự; nếu ký tự là chữ số thì bật cờ số, nếu là chữ cái thì bật cờ chữ. Có thể dùng `.isdigit()` và `.isalpha()` để kiểm tra một ký tự.
- Điều kiện độ dài dùng `len(mk) >= 8`.
- Cuối cùng `return` kết quả là phép AND của ba điều kiện (đủ dài, có số, có chữ). Đừng `return True` giữa chừng khi mới thỏa một điều kiện.

**Bài 3 — Fibonacci trả về danh sách**
- Xử lý biên trước khi vào vòng lặp: `n == 0` trả về `[]`; `n == 1` trả về `[0]`.
- Với `n >= 2`: bắt đầu danh sách bằng `[0, 1]`, rồi lặp thêm cho tới khi đủ `n` phần tử. Mỗi số mới bằng tổng hai số cuối của danh sách hiện tại (có thể lấy bằng chỉ số `-1` và `-2`).
- Dùng `append` để thêm số mới vào danh sách.
- Cuối hàm `return` danh sách.
