# Bài 12 — OOP cơ bản (class, object) · Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 12

Phần này **không cho lời giải hoàn chỉnh**. Mục tiêu là giúp bạn tự viết code: nên thiết kế class ra sao, các bước logic thế nào, và tránh cạm bẫy nào.

### Dễ

**Bài 1 & 2 — Class `Sach`.**
- `__init__` nhận `tieu_de`, `tac_gia` và gán vào `self.tieu_de`, `self.tac_gia`.
- Method `gioi_thieu(self)` dùng f-string in câu mô tả. Nhớ tham số đầu tiên luôn là `self`.
- Tạo object bằng `Sach("...", "...")` rồi gọi `.gioi_thieu()`.
- Cạm bẫy: gọi `Sach.gioi_thieu()` trực tiếp trên class (không qua object) sẽ lỗi thiếu `self`.

**Bài 3 — `HinhChuNhat`.**
- Lưu `chieu_dai`, `chieu_rong` trong `__init__`. Method `tinh_dien_tich(self)` **return** tích hai cạnh (return chứ không print, để dùng lại được).

**Bài 4 — `DienThoai`.**
- `__init__` cho `pin` có giá trị mặc định: `def __init__(self, pin=100)`.
- Method `su_dung(self, gio)`: giảm `self.pin` đi `gio * 10`; sau đó nếu `self.pin < 0` thì đặt lại về `0`.
- Cạm bẫy: kẹp giá trị (clamp) sau khi trừ, đừng để pin âm lọt ra ngoài.

**Bài 5 — Danh sách `SinhVien`.**
- Class có `ten`, `mssv`. Tạo một list gồm 3 object, rồi `for sv in danh_sach:` in `sv.ten`, `sv.mssv`.

### Trung bình

**Bài 1 — `TaiKhoanNganHang`.**
- `nap_tien`: cộng vào `self.so_du`.
- `rut_tien`: nếu `so_tien > self.so_du` thì `raise ValueError("...")` (ôn Bài 11) — không trừ; ngược lại trừ tiền.
- Khi dùng, bọc lệnh rút trong `try/except ValueError` để bắt và in thông báo thay vì để sập.

**Bài 2 — Kế thừa `PhuongTien`.**
- Class cha `PhuongTien` có `__init__` lưu `ten` và method `di_chuyen()`.
- Class con khai báo `class XeMay(PhuongTien):` và **ghi đè** `di_chuyen()` bằng nội dung riêng. Không cần viết lại `__init__` nếu dùng chung.
- In: bỏ các object vào một list rồi lặp gọi `.di_chuyen()` — mỗi loại tự in kiểu của mình (đa hình).

**Bài 3 — `GhiChu` + JSON.**
- Thuộc tính: `self.danh_sach = []`. Method `them(noi_dung)` dùng `append`.
- `luu_file(ten_file)`: mở chế độ `"w"`, `json.dump(self.danh_sach, f, ensure_ascii=False, indent=2)`.
- `tai_file(ten_file)`: mở `"r"`, `json.load` gán lại vào `self.danh_sach`.
- Cạm bẫy: cần `import json`. Nếu file có thể chưa tồn tại, cân nhắc `try/except FileNotFoundError` trong `tai_file`.

### Khó

**Bài 1 — Thư viện sách.**
- Thiết kế: `Sach` có `da_muon=False`. `ThuVien` có `self.ds_sach = []`.
- `muon(tieu_de)`: duyệt danh sách tìm sách khớp tiêu đề. Nếu không thấy → xử lý (raise hoặc thông báo). Nếu thấy nhưng `da_muon` đã `True` → `raise` lỗi "đã có người mượn". Ngược lại đặt `da_muon = True`.
- `tra` tương tự nhưng đặt lại `False`.
- `liet_ke_con_lai`: lặp và chỉ in sách có `da_muon == False`.
- Cạm bẫy: tìm sách theo tiêu đề nên chuẩn hóa (ví dụ `.strip()`, có thể `.lower()`) để tránh trượt vì khác khoảng trắng/hoa thường.

**Bài 2 — Nhân viên và lương (đa hình).**
- Cha `NhanVien`: `__init__(self, ten, luong_co_ban)`, `tinh_luong(self)` return `self.luong_co_ban`.
- `NhanVienToanThoiGian`: có thể thêm phụ cấp; ghi đè `tinh_luong` để trả về `luong_co_ban + phu_cap`. Nếu cần thêm thuộc tính riêng, định nghĩa `__init__` mới và gọi `super().__init__(...)` để tái dùng phần khởi tạo của cha.
- `NhanVienTheoGio`: `__init__` nhận `so_gio`, `luong_gio`; ghi đè `tinh_luong` trả về `so_gio * luong_gio`.
- In bảng lương: một list trộn cả hai loại, một vòng `for nv in ds:` gọi `nv.tinh_luong()`. Điểm mấu chốt: cùng một lời gọi, kết quả khác nhau tùy loại — đó là đa hình.
- Cạm bẫy: nhớ `super().__init__(...)` khi class con có `__init__` riêng, nếu không thuộc tính của cha sẽ không được thiết lập.

**Bài 3 — Sổ chi tiêu.**
- `KhoanChi.__init__(self, so_tien, danh_muc, ngay)` lưu ba thuộc tính.
- `SoChiTieu.them_khoan(...)`: kiểm tra `so_tien > 0`, nếu không thì `raise ValueError`; hợp lệ thì tạo `KhoanChi` và `append`.
- `tong_theo_danh_muc()`: duyệt các khoản, cộng dồn vào dict theo `danh_muc` (mẫu `d[dm] = d.get(dm, 0) + so_tien`).
- `luu(ten_file)`: vì `json.dump` không ghi trực tiếp object, hãy chuyển mỗi `KhoanChi` thành dict trước (ví dụ tạo một list dict `{"so_tien":..., "danh_muc":..., "ngay":...}`) rồi mới dump.
- `tai(ten_file)`: đọc JSON (một list dict), dựng lại các object `KhoanChi` từ từng dict; nếu file chưa tồn tại thì để danh sách rỗng (bắt `FileNotFoundError`).
- Cạm bẫy: `json.dump` không tự biết cách lưu object tùy biến → phải tự chuyển sang dict/list các kiểu cơ bản; khi tải lại thì tự dựng object từ dict. Đây chính là ý tưởng cốt lõi bạn sẽ dùng cho dự án quản lý chi tiêu cuối module.

---

⬅️ Quay lại [Mục lục bài](../README.md)
