# Sổ điểm — Bài 02: Biến & kiểu dữ liệu

> Track: Cơ bản (Beginner) · Ngày: 25-08-2026 · Thang điểm 10

## Tổng quan

| Mức độ | Điểm | File code |
|--------|:----:|-----------|
| Dễ (Easy) | 10 | `code/25-08-2026/easy-02-1.py` |
| Trung bình (Medium) | 10 | `code/25-08-2026/medium-02-1.py` |
| Khó (Hard) | — | *(chưa làm)* |

**Điểm trung bình bài: (đang cập nhật — còn mức Khó)**

## Nhận xét chi tiết

### Bài Dễ — 10/10 (ban đầu 8, sau khi sửa → 10)
- Cú pháp rất chắc: đủ dấu nháy, ngoặc, ép kiểu `int()`/`str()` đúng chỗ; dùng cả dấu phẩy trong `print`.
- Câu 1, 3, 4 đúng hoàn hảo ngay từ đầu.
- Hai lỗi ban đầu, tự sửa đúng sau khi được gợi mở (không đưa lời giải):
  - Câu 2: ban đầu in `type()` của biến cá nhân thay vì 4 giá trị đề cho (`100`, `3.14`, `"Python"`, `False`) → đã sửa in đúng kiểu.
  - Câu 5: nhầm "hiệu" dùng phép chia `a / b` → đã sửa thành phép trừ `a - b` (ra 7).

### Bài Trung bình — 10/10 (ban đầu 8, sau khi sửa → 10)
- Câu 3 (hoán đổi biến `x, y = y, x`) đúng ngay — nắm tốt cú pháp Pythonic.
- Công thức đổi độ C→F chính xác (ra 86.0).
- Hai điểm sửa sau gợi mở (không đưa lời giải):
  - Câu 1: ban đầu tính ra **số tiền giảm** (15000) thay vì **giá sau giảm** → sửa `gia_so - (gia_so*10/100)` = 135000.0.
  - Câu 2: gộp 2 dòng in thành 1 dòng đúng định dạng đề `30 độ C = 86.0 độ F`.

## Bài học rút ra
- Đọc kỹ **đúng yêu cầu đề**: "giá sau giảm" ≠ "số tiền giảm"; "hiệu" ≠ "thương".
- Phân biệt thuật ngữ toán: tổng (+), hiệu (−), tích (×), thương (÷).
- Code chạy được chưa chắc đúng ý đề — cần đối chiếu output với yêu cầu.
