# Bài 10 — Đọc/ghi file văn bản · Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 10

Phần này **không cho lời giải hoàn chỉnh**. Mục tiêu là giúp bạn tự viết code: nên dùng công cụ gì, các bước logic ra sao, và tránh cạm bẫy nào.

### Dễ

**Bài 1 — Ghi rồi đọc lại `hello.txt`.**
- Mở hai lần: lần đầu chế độ `"w"` để `f.write(...)`, lần sau chế độ `"r"` để `f.read()`.
- Luôn dùng khối `with` và thêm `encoding="utf-8"`.

**Bài 2 — Ghi 3 dòng món ăn.**
- Đặt các món vào một list, rồi vòng `for` ghi từng món. Nhớ nối `"\n"` vào cuối mỗi món để mỗi món nằm trên một dòng.
- Cạm bẫy: nếu quên `\n`, ba món sẽ dính liền thành một dòng.

**Bài 3 — Đếm số dòng.**
- Gợi ý: `f.readlines()` trả về list mỗi dòng là một phần tử, rồi `len(...)` cho số dòng.
- Cạm bẫy: nếu file kết thúc bằng một dòng trống, số đếm có thể lệch 1; hãy nghĩ xem dữ liệu của bạn có dòng trống cuối không.

**Bài 4 — Thêm món bằng chế độ `"a"`.**
- Mở với `"a"` để nối vào cuối, không xóa dữ liệu cũ. Ghi thêm các món mới (kèm `\n`).
- Sau đó mở lại `"r"` và lặp qua file in từng dòng, nhớ `.strip()` để bỏ `\n`.

**Bài 5 — Lưu profile ra JSON.**
- Cần `import json`. Tạo một `dict` gồm `ten` và `tuoi` (nhớ `int(...)` cho tuổi).
- Ghi: `json.dump(dict, f, ensure_ascii=False, indent=2)`.
- Đọc lại: `json.load(f)` trả về dict, rồi dùng f-string in câu chào.
- Cạm bẫy: `json.dump` (ghi file) khác `json.dumps` (ra chuỗi) — bài này dùng bản không có `s`.

### Trung bình

**Bài 1 — Đếm tổng số từ trong file.**
- Đọc toàn bộ bằng `f.read()` thành một chuỗi lớn, rồi `.split()` (không tham số) tách theo mọi khoảng trắng và xuống dòng; `len(...)` cho số từ.

**Bài 2 — Danh bạ JSON.**
- Trước khi đọc, cần xử lý trường hợp file chưa tồn tại. Gợi ý: `import os` và kiểm tra `os.path.exists(TEN_FILE)`; nếu chưa có thì bắt đầu bằng `[]`. (Hoặc dùng `try/except FileNotFoundError` — bạn sẽ học kỹ ở Bài 11.)
- Đọc bằng `json.load` → được list các dict. `append` một dict liên hệ mới. Ghi lại toàn bộ list bằng `json.dump`.
- In: lặp qua list, mỗi phần tử là dict, truy cập `lien_he["ten"]`, `lien_he["sdt"]`.

**Bài 3 — Đánh số dòng ra file mới.**
- Đọc file nguồn (lặp qua từng dòng hoặc `readlines`). Dùng `enumerate(..., start=1)` để có số thứ tự.
- Mở file đích chế độ `"w"`, ghi mỗi dòng dạng `f"{so}: {dong.strip()}\n"`.
- Cạm bẫy: nếu không `.strip()` dòng gốc rồi lại thêm `\n`, bạn có thể tạo ra dòng trống thừa vì dòng gốc đã có sẵn `\n`.

### Khó

**Bài 1 — Bộ đếm lượt chạy.**
- Bước đọc an toàn: nếu file `dem.txt` chưa tồn tại (kiểm tra bằng `os.path.exists` hoặc bắt lỗi), coi số hiện tại là `0`. Nếu tồn tại, đọc nội dung và `int(...)` nó.
- Tăng biến đếm lên 1, in thông báo, rồi mở chế độ `"w"` ghi số mới (nhớ `str(...)` vì `write` chỉ nhận chuỗi).
- Cạm bẫy: `write` không tự đổi số thành chuỗi — quên `str()` sẽ báo `TypeError`.

**Bài 2 — Top 3 từ hay gặp.**
- Đọc toàn bộ, `.lower()`, `.split()` để có list từ.
- Đếm bằng dict: `d[tu] = d.get(tu, 0) + 1` (ôn Bài 08).
- Sắp xếp giảm dần theo số lần: tìm hiểu `sorted(d.items(), key=..., reverse=True)` — `key` là một hàm chỉ ra "sắp theo giá trị nào" (ở đây là value, tức phần tử thứ hai của mỗi cặp). Sau đó lấy 3 phần tử đầu bằng slice `[:3]`.
- Cạm bẫy: dấu câu dính vào từ (ví dụ `python.`) sẽ bị đếm khác `python`. Nếu muốn chính xác hơn, cân nhắc loại dấu câu trước khi đếm (kỹ thuật từ Bài 09).

**Bài 3 — Nhật ký công việc JSON nhóm theo ưu tiên.**
- Đọc an toàn như Bài Trung bình 2 (file chưa có → list rỗng).
- Mỗi công việc là dict `{"tieu_de": ..., "uu_tien": ...}`. `append` cái mới rồi `json.dump` lưu lại.
- Nhóm khi in: có thể lọc hai lần — một vòng lặp in các việc có `uu_tien == "cao"`, rồi một vòng nữa cho `"thap"`. Hoặc gom vào hai list riêng trước khi in.
- Cạm bẫy: nếu người dùng nhập ưu tiên với chữ hoa/thường lẫn lộn ("Cao", "CAO"), việc so sánh sẽ trượt. Cân nhắc `.lower().strip()` giá trị nhập vào trước khi lưu để dữ liệu đồng nhất.

---

⬅️ Quay lại [Mục lục bài](../README.md)
