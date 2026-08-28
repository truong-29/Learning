# Bài 08 — Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 08

Trang này **không cho lời giải sẵn**. Mỗi bài chỉ gợi mở hướng đi, các bước logic và cạm bẫy cần tránh để bạn **tự viết** code.

## Dễ

**Bài 1 — Dictionary thông tin bản thân**
- Tạo dictionary với các key `"ten"`, `"tuoi"`, `"so_thich"`.
- Duyệt bằng `for key, value in dict.items()` rồi in cặp key–value bằng f-string.

**Bài 2 — Điểm 3 môn, in và cập nhật**
- Tạo dictionary với key là tên môn. Lấy điểm Toán bằng `dict["Toán"]`.
- Cập nhật chỉ cần gán lại: `dict["Toán"] = giá_trị_mới`.

**Bài 3 — Thêm và xóa môn**
- Thêm môn mới bằng cách gán key chưa có. Xóa bằng `del dict["tên_môn"]`.
- Cạm bẫy: xóa một key không tồn tại sẽ báo `KeyError`; hãy chắc key có thật.

**Bài 4 — Loại trùng bằng set**
- Chuyển list thành set bằng `set(list)`. Set tự loại phần tử trùng.
- Nếu cần kiểu list, bọc lại bằng `list(...)`.

**Bài 5 — Giao và hợp**
- Giao (phần chung) dùng toán tử `&`; hợp dùng `|`. In trực tiếp kết quả.

## Trung bình

**Bài 1 — Đếm ký tự (bỏ khoảng trắng)**
- Chuẩn bị dictionary rỗng.
- Duyệt từng ký tự trong câu; nếu ký tự là khoảng trắng thì `continue` để bỏ qua.
- Với ký tự khác: nếu đã là key thì cộng thêm 1, chưa có thì đặt bằng 1. Mẹo gọn hơn: dùng `dem.get(ky_tu, 0) + 1` để lấy giá trị hiện tại (mặc định 0 nếu chưa có).
- Cuối cùng duyệt `items()` để in.

**Bài 2 — Môn điểm cao nhất**
- Chuẩn bị hai biến: tên môn cao nhất (chuỗi rỗng) và điểm cao nhất (số rất nhỏ, ví dụ -1).
- Duyệt `items()`; nếu điểm hiện tại lớn hơn điểm cao nhất đang giữ thì cập nhật cả hai biến.
- Cạm bẫy: đừng chỉ so sánh value mà quên lưu lại tên môn tương ứng.

**Bài 3 — Bạn chung và riêng**
- Đổi hai list thành set.
- Bạn chung = phép giao `&`. Người chỉ có ở list thứ nhất = phép hiệu `-` (set A trừ set B).

## Khó

**Bài 1 — Sổ danh bạ mini**
- Dùng một dictionary `danh_ba` làm nơi lưu, key là tên, value là số điện thoại.
- Khung ngoài là `while True` in menu, đọc lựa chọn, rồi dùng `if/elif` cho từng chức năng. Thoát bằng `break` khi chọn 5.
- Thêm/cập nhật: gán `danh_ba[ten] = so` — cùng một cú pháp cho cả hai (gán đè nếu đã tồn tại).
- Tra và xóa: kiểm tra `if ten in danh_ba` trước; nếu không có thì in "Không tìm thấy". Đây là phần xử lý biên bắt buộc để tránh `KeyError`.
- In toàn bộ: duyệt `items()`. Nhớ trường hợp danh bạ rỗng thì in thông báo trống.

**Bài 2 — Từ phổ biến nhất**
- Trước tiên tách câu thành list từ bằng `split()` và đếm tần suất vào dictionary (giống ví dụ đếm từ trong bài lý thuyết).
- Tìm số lần lớn nhất: có thể lấy `max(dem.values())`.
- Sau đó duyệt `items()` và thu thập **mọi** từ có tần suất bằng số lớn nhất đó vào một list — nhờ vậy xử lý được trường hợp đồng hạng.
- Cạm bẫy: đừng dừng ở từ đầu tiên đạt max; phải quét hết để bắt các từ đồng hạng.

**Bài 3 — So sánh môn hai học kỳ**
- Cả hai kỳ đều có: phép giao `&`.
- Chỉ có ở kỳ 1 (đã bỏ): hiệu `ky1 - ky2`.
- Mới ở kỳ 2: hiệu `ky2 - ky1`.
- Toàn bộ đã từng học: hợp `|`.
- Cạm bẫy: chú ý thứ tự khi trừ, vì `A - B` khác `B - A`.
