# Bài 05 — Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 05

Trang này **không cho lời giải sẵn**. Mỗi bài chỉ gợi mở hướng đi, các bước logic và cạm bẫy cần tránh để bạn **tự viết** code.

## Dễ

**Bài 1 — In số 1 đến 20**
- Dùng `for` với `range`. Nhớ `range(1, 21)` mới cho ra tới 20 (giá trị `stop` không được in).
- Trong thân vòng lặp chỉ cần một lệnh `print`.

**Bài 2 — Số chẵn 2 đến 30**
- Vẫn là `for` + `range`, nhưng thêm **bước nhảy** (tham số thứ ba). Bắt đầu từ 2, mỗi bước cộng 2.
- Cạm bẫy: nếu muốn tới đúng 30 thì `stop` phải lớn hơn 30 (ví dụ 31), vì `stop` không được lấy.

**Bài 3 — Tổng 1 đến 100**
- Cần một biến "tích lũy" khởi tạo bằng 0 **trước** vòng lặp.
- Mỗi vòng cộng dồn giá trị hiện tại vào biến đó. In biến sau khi vòng lặp kết thúc (in ngoài vòng lặp, không phải trong).
- Kết quả đúng là 5050 để bạn tự đối chiếu.

**Bài 4 — Bảng cửu chương của n**
- Dùng `input` rồi `int(...)` để đổi chuỗi thành số.
- Lặp biến `i` từ 1 tới 10, mỗi dòng in `n x i = tích`. Dùng f-string sẽ gọn: `f"{n} x {i} = {n*i}"`.

**Bài 5 — Nhập mật khẩu tới khi đúng**
- Đây là tình huống "chưa biết trước số lần" → dùng `while`.
- Ý tưởng: giữ một biến chứa mật khẩu đã nhập, lặp **chừng nào** nó khác `"python"`.
- Cạm bẫy: phải cho biến một giá trị ban đầu khác `"python"` để vòng lặp chạy lần đầu; và bên trong vòng lặp phải gọi lại `input` để có cơ hội thoát.

## Trung bình

**Bài 1 — Kiểm tra số nguyên tố**
- Định nghĩa: số nguyên tố là số ≥ 2 và chỉ chia hết cho 1 và chính nó.
- Xử lý biên trước: nếu `n < 2` thì chắc chắn không phải nguyên tố.
- Ý tưởng chính: dùng một biến cờ (ví dụ `la_nguyen_to = True`), rồi thử chia `n` cho các số từ 2 tới `n-1`. Nếu chia hết một lần thì đặt cờ về `False` và `break` để dừng sớm.
- Toán tử `%` cho phần dư; `n % i == 0` nghĩa là chia hết.

**Bài 2 — Tam giác dấu sao**
- Lặp biến `dong` từ 1 tới `n`.
- Mẹo: chuỗi nhân với số sẽ lặp lại chuỗi, ví dụ `"*" * dong` cho ra số sao bằng `dong`. In chuỗi đó mỗi vòng.

**Bài 3 — Giai thừa**
- Cần biến tích lũy khởi tạo bằng **1** (không phải 0, vì đây là phép nhân).
- Lặp từ 1 tới `n`, mỗi vòng nhân dồn biến với giá trị đếm.
- Cạm bẫy: `range(1, n)` sẽ thiếu chính số `n`; cần `range(1, n+1)`.

## Khó

**Bài 1 — Máy tính bỏ túi mini**
- Khung ngoài là `while True` (lặp mãi) và chỉ thoát bằng `break` khi người dùng gõ `thoat`.
- Các bước mỗi vòng: nhận đầu vào, kiểm tra có phải `thoat` không → nếu đúng thì `break`; nếu không thì tách toán hạng và toán tử.
- Cách tách đơn giản cho người mới: hỏi lần lượt số thứ nhất, phép tính, số thứ hai (ba lần `input`) thay vì phân tích cả một chuỗi.
- Dùng `if/elif` để xử lý từng phép `+ - * /`.
- Trường hợp biên bắt buộc: khi phép chia và số thứ hai bằng 0, **không** thực hiện phép chia — in thông báo lỗi rồi `continue` để quay lại đầu vòng. Đừng để chương trình sập.

**Bài 2 — Số nguyên tố nhỏ hơn N**
- Đây là vòng lặp lồng nhau: vòng ngoài duyệt từng số `so` từ 2 tới N; vòng trong kiểm tra `so` có nguyên tố không (dùng lại ý tưởng cờ + `break` ở bài Trung bình 1).
- Tối ưu: chỉ cần thử ước từ 2 tới phần nguyên của căn bậc hai của `so`. Bạn có thể so sánh `i * i <= so` thay vì tính căn để tránh phải nhập thêm thư viện.
- In số ra khi vòng trong xác nhận nó là nguyên tố.

**Bài 3 — Kim tự tháp căn giữa**
- Lặp `dong` từ 1 tới `n`. Với mỗi dòng cần tính hai phần: số khoảng trắng bên trái và số sao.
- Quan sát quy luật: số sao là số lẻ `2*dong - 1`; số khoảng trắng bên trái là `n - dong`.
- Ghép chuỗi: `" " * số_khoảng_trắng + "*" * số_sao` rồi in. Tự thử với `n = 4` để đối chiếu hình mẫu.
- Cạm bẫy: nếu thiếu phần khoảng trắng, tháp sẽ lệch về bên trái thay vì cân giữa.
