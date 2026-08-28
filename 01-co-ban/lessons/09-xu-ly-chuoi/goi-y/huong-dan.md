# Bài 09 — Xử lý chuỗi · Gợi ý hướng dẫn

> Track: Cơ bản (Beginner) · Module 1 · Bài 09

Phần này **không cho lời giải hoàn chỉnh**. Mục tiêu là giúp bạn tự viết code: nên dùng công cụ gì, các bước logic ra sao, và tránh cạm bẫy nào. Hãy đọc gợi ý rồi tự gõ.

### Dễ

**Bài 1 — Độ dài, ký tự đầu/cuối.**
- Công cụ: `len()` để lấy độ dài, index `[0]` cho ký tự đầu, index `[-1]` cho ký tự cuối.
- Cạm bẫy: nếu người dùng nhập chuỗi rỗng thì `[0]` sẽ báo `IndexError`. Thử nghĩ xem có nên kiểm tra `len(s) > 0` trước không.

**Bài 2 — HOA / thường toàn bộ.**
- Công cụ: hai method `.upper()` và `.lower()`. Nhớ chúng **trả về chuỗi mới**, không sửa chuỗi gốc.
- Chỉ cần `print` trực tiếp kết quả của mỗi method.

**Bài 3 — Đếm số từ.**
- Ý tưởng: `.split()` (không tham số) tách câu thành list các từ, tự gộp khoảng trắng thừa. Sau đó `len()` của list đó là số từ.
- Cạm bẫy: nếu dùng `.split(" ")` (có tham số khoảng trắng) thì khoảng trắng thừa sẽ tạo ra phần tử rỗng, làm sai số đếm. Ưu tiên `.split()` không tham số.

**Bài 4 — Đảo ngược chuỗi.**
- Mẹo slice: `s[::-1]` đọc là "lấy toàn bộ với bước nhảy -1" → đảo ngược.

**Bài 5 — Chuẩn hóa khoảng trắng hai đầu.**
- Công cụ: `.strip()` bỏ khoảng trắng ở hai đầu.
- Để "thấy rõ" kết quả, in kèm dấu nháy bao quanh, ví dụ dùng f-string dạng `f"'{...}'"`. Nhờ đó bạn nhìn được biên của chuỗi.

### Trung bình

**Bài 1 — Palindrome.**
- Các bước: (1) chuẩn hóa chuỗi về cùng dạng để so sánh công bằng — `.lower()` để bỏ khác biệt hoa/thường, có thể `.replace(" ", "")` để bỏ khoảng trắng; (2) so sánh chuỗi đã chuẩn hóa với bản đảo ngược `[::-1]` của chính nó; (3) nếu bằng nhau thì là palindrome.
- Cạm bẫy: nếu quên chuẩn hóa, "Radar" sẽ không được coi là palindrome vì `R` khác `r`.

**Bài 2 — Kiểm tra email đơn giản.**
- Điều kiện 1: đúng một dấu `@`. Gợi ý: `chuoi.count("@")` đếm số lần xuất hiện — cần bằng `1`.
- Điều kiện 2: phần sau `@` phải chứa `.`. Gợi ý: tách bằng `.split("@")` để lấy phần domain (phần tử thứ hai), rồi kiểm tra `"." in domain`.
- Kết hợp hai điều kiện bằng `and` trong một câu `if`.
- Cạm bẫy: `"a@@b.com"` có 2 dấu `@` → không hợp lệ; hãy chắc điều kiện `count == 1` chặn được nó.

**Bài 3 — Viết hoa chữ đầu và nối bằng gạch nối.**
- Các bước: (1) `.split()` để tách thành list từ; (2) duyệt từng từ, dùng `.capitalize()` để viết hoa chữ cái đầu mỗi từ; (3) gom các từ đã viết hoa lại rồi `"-".join(...)`.
- Có thể duyệt bằng vòng `for` + `append` (Bài 05 & 07), hoặc tìm hiểu cách viết gọn hơn. Tự chọn cách bạn thấy dễ hiểu.
- Cạm bẫy: `.title()` cũng viết hoa chữ đầu nhưng xử lý ký tự đặc biệt hơi khác `.capitalize()`; với bài này `.capitalize()` từng-từ là an toàn nhất.

### Khó

**Bài 1 — Chuẩn hóa danh sách tên nhiều dòng.**
- Bước 1: tách chuỗi lớn thành từng dòng bằng `.split("\n")`.
- Bước 2: duyệt từng dòng; với mỗi dòng, `.strip()` rồi kiểm tra: nếu sau strip là chuỗi rỗng thì **bỏ qua** (đây là cách loại dòng trống).
- Bước 3: chuẩn hóa từng tên còn lại — `.split()` (gộp khoảng trắng giữa), viết hoa chữ đầu mỗi từ (như bài Trung bình 3), rồi `" ".join(...)`.
- Bước 4: in kèm số thứ tự. `enumerate(..., start=1)` giúp đánh số từ 1.
- Cạm bẫy: đừng đánh số theo index dòng gốc, vì dòng trống bị loại sẽ làm số nhảy cách. Hãy đánh số theo danh sách tên **đã lọc**.

**Bài 2 — Tần suất ký tự.**
- Chuẩn hóa trước: `.lower()` và loại khoảng trắng (`.replace(" ", "")`).
- Đếm: dùng một `dict` với key là ký tự, value là số lần. Mẫu nhỏ để cộng dồn an toàn: `d[ch] = d.get(ch, 0) + 1` (`.get` trả 0 nếu key chưa có). Ôn lại Bài 08 về dict.
- Tìm max: trước hết tìm số lần lớn nhất bằng `max(d.values())`, sau đó duyệt dict lấy tất cả ký tự có value bằng số đó (để xử lý trường hợp hòa).
- Cạm bẫy: nếu chỉ dùng `max(d, key=d.get)` bạn chỉ lấy **một** ký tự, sẽ bỏ sót trường hợp nhiều ký tự cùng cao nhất.

**Bài 3 — Tạo slug.**
- Bước 1: `.strip()` rồi `.lower()`.
- Bước 2: loại ký tự đặc biệt. Ý tưởng: duyệt từng ký tự, chỉ giữ ký tự nếu nó là chữ/số (thử method kiểm tra như `.isalnum()`) hoặc là khoảng trắng; ký tự khác thì bỏ. Gom lại thành chuỗi mới.
- Bước 3: `.split()` để gộp khoảng trắng thừa thành list từ, rồi `"-".join(...)`. Cách này tự động tránh dấu `-` thừa ở đầu/cuối và hai dấu `-` liền nhau, vì `.split()` đã loại mọi khoảng trắng rỗng.
- Cạm bẫy: nếu bạn thay khoảng trắng bằng `-` bằng `.replace(" ", "-")` một cách thô, các khoảng trắng thừa sẽ sinh ra `--` và có thể để `-` ở hai đầu. Dùng `split()` + `join()` sạch hơn nhiều.

---

⬅️ Quay lại [Mục lục bài](../README.md)
