# Bài 12 — OOP cơ bản (class, object) · Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 12
>
> **Độ khó: Khó (Hard)**

Đây là các bài tổng hợp cuối Module 1: kết hợp class, kế thừa, xử lý lỗi (Bài 11) và lưu/đọc JSON (Bài 10). Hãy vạch thiết kế class (thuộc tính, method) trước khi code.

1. **Quản lý thư viện sách.** Tạo class `Sach` (`tieu_de`, `tac_gia`, `da_muon` mặc định `False`) và class `ThuVien` chứa một danh sách các object `Sach`. `ThuVien` có các method: `them_sach(sach)`, `muon(tieu_de)` (đánh dấu đã mượn, nếu sách đã được mượn rồi thì `raise` lỗi), `tra(tieu_de)` (đánh dấu trả lại), và `liet_ke_con_lai()` (in các sách chưa bị mượn). Xử lý trường hợp mượn/trả một tiêu đề không tồn tại.

2. **Hệ thống nhân viên với kế thừa và tính lương.** Tạo class cha `NhanVien` (`ten`, `luong_co_ban`) với method `tinh_luong()` trả về lương cơ bản. Tạo hai class con: `NhanVienToanThoiGian` (cộng thêm phụ cấp cố định) và `NhanVienTheoGio` (`so_gio`, `luong_gio`; lương = số giờ × lương giờ, ghi đè `tinh_luong()`). Tạo một danh sách trộn cả hai loại nhân viên rồi in bảng lương của tất cả bằng một vòng lặp duy nhất (đây là sức mạnh của kế thừa: cùng gọi `tinh_luong()` nhưng mỗi loại tính theo cách riêng).

3. **Sổ quản lý chi tiêu tối giản (tiền đề cho dự án cuối module).** Tạo class `KhoanChi` (`so_tien`, `danh_muc`, `ngay`) và class `SoChiTieu` chứa danh sách các `KhoanChi`. `SoChiTieu` có method: `them_khoan(so_tien, danh_muc, ngay)` (kiểm tra `so_tien > 0`, nếu không thì `raise ValueError`), `tong_theo_danh_muc()` (trả về dict tổng tiền mỗi danh mục), `luu(ten_file)` (ghi toàn bộ ra JSON) và `tai(ten_file)` (đọc lại từ JSON, nếu file chưa tồn tại thì bắt đầu bằng sổ rỗng). Đây gần như là bản thu nhỏ của dự án cuối module.

---

⬅️ Quay lại [Độ khó Trung bình](trung-binh.md) · 💡 Bí thì xem [gợi ý hướng dẫn](../goi-y/huong-dan.md)
