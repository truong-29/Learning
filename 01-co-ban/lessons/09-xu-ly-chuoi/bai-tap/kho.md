# Bài 09 — Xử lý chuỗi · Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 09
>
> **Độ khó: Khó (Hard)**

Các bài này gần với bài toán thực tế: dữ liệu bẩn, nhiều trường hợp biên, phải kết hợp nhiều kỹ thuật chuỗi đã học. Đọc kỹ yêu cầu và tự vạch các bước trước khi code.

1. **Chuẩn hóa danh sách tên nhiều dòng.** Cho một chuỗi nhiều dòng, mỗi dòng là một họ tên nhập lộn xộn (khoảng trắng thừa ở hai đầu và ở giữa, hoa/thường tùy tiện), ví dụ:
   ```
   "  nguyen   VAN an \n tran thi   BINH\n\n  le  hoang C  "
   ```
   Hãy in ra danh sách đã chuẩn hóa: mỗi dòng một tên, bỏ dòng trống, mỗi từ viết hoa chữ cái đầu, giữa các từ đúng một khoảng trắng. Kết quả mong đợi:
   ```
   1. Nguyen Van An
   2. Tran Thi Binh
   3. Le Hoang C
   ```

2. **Đếm tần suất ký tự và tìm ký tự xuất hiện nhiều nhất.** Nhập một câu, bỏ qua khoảng trắng và không phân biệt hoa/thường. Đếm mỗi chữ cái xuất hiện bao nhiêu lần và in ra chữ cái xuất hiện nhiều nhất cùng số lần. Xử lý được trường hợp có nhiều chữ cùng đạt số lần cao nhất (in tất cả).

3. **Tạo "slug" cho tiêu đề bài viết.** Nhập một tiêu đề bất kỳ (có thể có khoảng trắng thừa, chữ hoa, và một vài ký tự đặc biệt như `! ? , .`). Hãy biến nó thành slug dùng cho URL: toàn chữ thường, các ký tự đặc biệt bị loại bỏ, các khoảng trắng thay bằng dấu `-`, không có dấu `-` thừa ở đầu/cuối hay hai dấu `-` liền nhau. Ví dụ: `"  Hoc Python That Vui!!  "` → `"hoc-python-that-vui"`.

---

⬅️ Quay lại [Độ khó Trung bình](trung-binh.md) · 💡 Bí thì xem [gợi ý hướng dẫn](../goi-y/huong-dan.md)
