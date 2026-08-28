# Bài 11 — Xử lý lỗi (try/except) · Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 11

Phần này **không cho lời giải hoàn chỉnh**. Mục tiêu là giúp bạn tự viết code: nên dùng công cụ gì, các bước logic ra sao, và tránh cạm bẫy nào.

### Dễ

**Bài 1 — Nhập số, chữ thì báo lỗi.**
- Đặt `int(input(...))` trong khối `try`. Lỗi khi ép "abc" thành số là `ValueError`; bắt đúng loại đó và in thông báo.

**Bài 2 — Chia hai số.**
- Đặt phép chia trong `try`. Bắt `ZeroDivisionError` cho trường hợp chia 0. Nên thêm cả `except ValueError` phòng khi người dùng nhập chữ.
- Cạm bẫy: nhớ bắt `ZeroDivisionError` riêng với `ValueError`, đừng gộp thành một `except` chung chung.

**Bài 3 — Mở file không tồn tại.**
- Đặt `with open("khong_ton_tai.txt", "r", ...)` trong `try`. Loại lỗi cần bắt là `FileNotFoundError`.

**Bài 4 — Tra điểm học sinh.**
- Truy cập `diem[ten]` trong `try`. Nếu key không có, Python ném `KeyError`; bắt nó và báo "Không có học sinh này".
- Mẹo: đây là lý do người ta hay dùng `.get()` cho dict, nhưng bài này cố ý luyện bắt `KeyError`.

**Bài 5 — try/except/finally.**
- `try`: ép số và tính bình phương. `except ValueError`: báo không hợp lệ. `finally`: in "Kết thúc chương trình".
- Cạm bẫy: `finally` **luôn** chạy — kể cả khi có lỗi lẫn khi không. Đừng đặt phần in kết quả tính toán vào `finally`.

### Trung bình

**Bài 1 — `chia_an_toan(a, b)`.**
- Trong hàm, `try` trả về `a / b`; `except ZeroDivisionError` in cảnh báo và `return None`.
- Test: gọi hàm với cặp chia được và cặp có `b = 0`, in kết quả để thấy `None`.
- Cạm bẫy: đảm bảo `return None` nằm trong nhánh `except`, đừng để hàm rơi xuống trả về ngầm ở cả hai đường.

**Bài 2 — Nhập tuổi hợp lệ, nhập lại đến khi đúng.**
- Dùng vòng `while True`. Trong `try`: ép số; nếu tuổi `< 0` hoặc `> 150` thì `raise ValueError("...")`.
- `except ValueError as e`: in lý do rồi để vòng lặp chạy tiếp (không `return`). Khi hợp lệ, dùng `break` hoặc `return` để thoát.
- Cạm bẫy: một `except ValueError` bắt được cả lỗi ép kiểu lẫn lỗi bạn tự `raise` — tận dụng điều đó thay vì viết hai nhánh.

**Bài 3 — Đọc JSON an toàn.**
- Trong hàm, `try` mở file và `json.load`.
- Hai nhánh `except` riêng: `FileNotFoundError` (không có file) và `json.JSONDecodeError` (nội dung hỏng), mỗi nhánh `return {}`.
- Cần `import json`. Cạm bẫy: `json.JSONDecodeError` là lớp con của `ValueError`; hãy bắt đúng tên để thông báo rõ ràng.

### Khó

**Bài 1 — Máy tính bỏ túi chống sập.**
- Khung: `while True` cho từng lượt tính. Bên trong dùng `try/except/finally`.
- `try`: ép hai số (`ValueError` nếu gõ chữ); đọc phép toán; nếu phép toán không thuộc `+ - * /` thì `raise ValueError("Phep toan khong hop le")`; thực hiện phép (chia có thể `ZeroDivisionError`).
- Nhiều `except`: `ValueError` cho nhập sai/phép sai, `ZeroDivisionError` cho chia 0.
- `finally`: in dòng ngăn cách — nó chạy sau mọi lượt bất kể thành công hay lỗi.
- Chọn tiếp tục: hỏi người dùng, nếu không tiếp thì `break`.
- Cạm bẫy: đặt `raise` cho phép toán sai **bên trong** `try` thì mới bị `except` bắt; nếu để ngoài, chương trình vẫn sập.

**Bài 2 — Nhập điểm hợp lệ vào danh sách.**
- Danh sách rỗng ban đầu. Vòng lặp: đọc input; nếu là `"xong"` thì dừng.
- Ép điểm trong `try`; kiểm tra khoảng `0..10`, ngoài khoảng thì `raise ValueError`. Lỗi → in lý do và cho nhập lại (không thêm vào danh sách). Hợp lệ → `append`.
- Trước khi tính trung bình, kiểm tra `len(danh_sach) > 0` để tránh `ZeroDivisionError` khi chưa nhập điểm nào.
- Cạm bẫy: việc kiểm tra "xong" nên làm **trước** khi ép kiểu, nếu không `int("xong")` sẽ ném lỗi.

**Bài 3 — Đọc cấu hình JSON với mặc định.**
- Chuẩn bị một dict cấu hình mặc định (ví dụ `{"ten_ung_dung": "App", ...}`).
- `try`: mở file, `json.load`. Sau khi load thành công, kiểm tra key bắt buộc: nếu thiếu, tự `raise KeyError("ten_ung_dung")` (hoặc kiểm tra bằng `if "..." not in data`).
- Ba nhánh phân biệt nguyên nhân: `except FileNotFoundError` (không có file), `except json.JSONDecodeError` (JSON hỏng), `except KeyError` (thiếu key). Mỗi nhánh in cảnh báo riêng rồi trả về cấu hình mặc định.
- Cạm bẫy: nếu bạn muốn giữ các giá trị hợp lệ đã đọc được nhưng bù key thiếu, hãy nghĩ tới việc trộn dict mặc định với dict đã đọc thay vì vứt bỏ toàn bộ — tùy mức độ bạn muốn làm kỹ.

---

⬅️ Quay lại [Mục lục bài](../README.md)
