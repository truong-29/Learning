# Bài 07 — Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 07

Trang này **không cho lời giải sẵn**. Mỗi bài chỉ gợi mở hướng đi, các bước logic và cạm bẫy cần tránh để bạn **tự viết** code.

## Dễ

**Bài 1 — 5 trái cây, in đầu và cuối**
- Tạo list bằng ngoặc vuông. Phần tử đầu là chỉ số `0`, phần tử cuối tiện nhất là chỉ số `-1`.

**Bài 2 — Tổng, max, min**
- Không cần tự viết vòng lặp: dùng thẳng các hàm dựng sẵn `sum(...)`, `max(...)`, `min(...)` với list.

**Bài 3 — Thêm cuối, chèn đầu**
- `append(x)` thêm vào cuối. Muốn chèn vào đầu thì dùng `insert(0, x)` (vị trí 0).
- In list ra sau mỗi thao tác để quan sát thay đổi.

**Bài 4 — Slice**
- 3 phần tử đầu: `list[:3]`. 2 phần tử cuối: `list[-2:]`.
- Nhớ `stop` trong slice không được lấy, nên `[:3]` cho các vị trí 0, 1, 2.

**Bài 5 — Tuple màu**
- Tạo tuple bằng ngoặc tròn. Duyệt bằng `for` giống hệt list; tuple chỉ khác ở chỗ không sửa được.

## Trung bình

**Bài 1 — Đếm chẵn/lẻ**
- Chuẩn bị hai biến đếm bằng 0.
- Duyệt từng phần tử; dùng `% 2 == 0` để nhận biết số chẵn, ngược lại là lẻ. Tăng biến đếm tương ứng.

**Bài 2 — Nhập tới khi gõ "xong"**
- Bắt đầu bằng list rỗng và một vòng `while True`.
- Mỗi vòng: nhận `input`. Nếu bằng `"xong"` thì `break`. Nếu không, đổi sang số bằng `int(...)` rồi `append` vào list.
- Sau vòng lặp: cạm bẫy quan trọng là list có thể **rỗng** (người dùng gõ "xong" ngay). Kiểm tra `len(list) > 0` trước khi tính trung bình để tránh chia cho 0.
- Trung bình = `sum(list) / len(list)`.

**Bài 3 — Loại bỏ trùng lặp (giữ thứ tự)**
- Tạo một list mới rỗng.
- Duyệt list gốc; với mỗi phần tử, chỉ `append` vào list mới **nếu nó chưa có** trong list mới (kiểm tra bằng `not in`).
- Cách này giữ nguyên thứ tự xuất hiện, khác với việc dùng `set`.

## Khó

**Bài 1 — Bảng xếp hạng điểm**
- Xử lý biên đầu tiên: nếu list rỗng thì in thông báo và dừng.
- Cần sắp xếp theo điểm giảm dần. Mỗi phần tử là tuple `(ten, diem)`, điểm nằm ở chỉ số 1. Bạn có thể dùng `sorted(danh_sach, key=..., reverse=True)`, trong đó `key` là một hàm nhỏ trả về phần tử điểm của mỗi tuple (ví dụ dùng `lambda item: item[1]`).
- Sau khi sắp xếp, duyệt bằng `enumerate(..., start=1)` để có số thứ hạng và in `tên - điểm`.
- Cạm bẫy: tránh nhầm chỉ số — tên là `[0]`, điểm là `[1]`.

**Bài 2 — Gộp và thống kê hai lớp**
- Gộp hai list: dùng toán tử `+` hoặc `extend`.
- Tổng số học sinh là `len` của list gộp; kiểm tra khác 0 trước khi chia.
- Trung bình chung = `sum / len`; làm tròn khi in bằng f-string `{tb:.2f}`.
- Đếm số bạn trên trung bình: duyệt list gộp, so sánh từng điểm với trung bình chung, tăng biến đếm khi lớn hơn.
- Cạm bẫy: tính trung bình **trước**, rồi mới đếm số bạn vượt trung bình (đừng đếm khi chưa biết ngưỡng).

**Bài 3 — Xoay vòng danh sách**
- Ý tưởng dùng slice: xoay phải `k` bước nghĩa là ghép `k` phần tử cuối lên trước phần còn lại. Với slice: phần cuối là `list[-k:]`, phần đầu là `list[:-k]`, rồi cộng hai phần lại.
- Trường hợp biên bắt buộc: nếu `k` lớn hơn `len(list)`, giá trị xoay thực chất lặp lại. Chuẩn hóa bằng `k = k % len(list)` trước khi cắt.
- Cạm bẫy: khi `k` bằng 0 (sau khi lấy dư), slice `list[-0:]` sẽ ra cả list — hãy thử và xử lý để kết quả vẫn là list gốc.
