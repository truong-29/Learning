# Bài 01 — Gợi ý hướng dẫn (KHÔNG phải lời giải)

> Track: Cơ bản (Beginner) · Module 1 · Bài 01

Dưới đây là hướng dẫn gợi mở để bạn **tự viết** code. Ở đây không có lời giải hoàn chỉnh — hãy đọc hướng dẫn, hiểu ý tưởng, rồi tự gõ.

### Dễ

1. Chỉ cần một lệnh `print`. Nhớ bọc câu chữ trong dấu nháy `"..."`. Cạm bẫy: gõ đúng dấu chấm than ở cuối như đề yêu cầu.
2. Ba thông tin riêng biệt → ba lệnh `print`, mỗi lệnh in một dòng. Mỗi lần gọi `print` tự động xuống dòng mới, nên không cần làm gì thêm.
3. Một dòng 5 dấu sao là chuỗi `"*****"`. Muốn 3 dòng giống nhau thì gọi `print` với chuỗi đó 3 lần. Cạm bẫy: đếm đúng 5 dấu sao mỗi dòng.
4. Hai câu → hai lệnh `print`. Chép chính xác dấu câu trong đề vào trong dấu nháy.
5. Tạo file tên `about_me.py` (đuôi `.py`), viết tối thiểu 4 lệnh `print` tự giới thiệu. Sau đó mở terminal ở đúng thư mục chứa file và chạy `python about_me.py`. Cạm bẫy: nếu terminal báo "không tìm thấy file", nghĩa là bạn đang đứng sai thư mục.

### Trung bình

1. Khung viền chỉ là các dòng chữ cố định. Hãy in lần lượt: dòng khung trên (các dấu `+` và `-`), dòng giữa chứa tên (bắt đầu và kết thúc bằng `|`), rồi dòng khung dưới. Mẹo: đếm số dấu `-` ở dòng trên và canh sao cho độ rộng của cả ba dòng bằng nhau.
2. Kim tự tháp 4 tầng: mỗi tầng là một lệnh `print`. Với mỗi tầng, phần đầu là các dấu cách, phần sau là các dấu sao. Quan sát quy luật: đi xuống một tầng thì bớt 1 dấu cách và thêm 2 dấu sao. Cạm bẫy: dấu cách ở đầu chuỗi cũng được in ra, nên phải gõ đúng số lượng.
3. Ký hiệu `\n` nằm bên trong một chuỗi sẽ tạo ra một lần xuống dòng. Vậy để in 2 dòng bằng một `print`, hãy đặt `\n` vào giữa hai phần nội dung trong cùng một chuỗi. Ví dụ dạng gọi hàm: `print("...\n...")`.

### Khó

1. **Hóa đơn có khung.** Đây là bài luyện căn cột. Hãy quyết định trước độ rộng bên trong khung (số ký tự giữa hai dấu `|`), rồi mọi dòng đều phải đủ đúng độ rộng đó. Chiến lược từng bước: (a) in dòng khung trên gồm `+`, một loạt `-`, rồi `+`; (b) mỗi dòng nội dung bắt đầu bằng `| `, phần chữ, một số dấu cách để đẩy giá tiền sang phải, rồi kết thúc bằng ` |`; (c) chèn dòng khung ngăn cách giữa tiêu đề, danh sách và tổng cộng. Cạm bẫy lớn nhất: số dấu cách phải khớp để các cạnh `|` thẳng hàng — hãy đếm cẩn thận hoặc dùng font đều (monospace) để nhìn cho dễ.
2. **Danh thiếp một lệnh.** Ràng buộc là chỉ một `print`. Nối 4 dòng thành một chuỗi duy nhất, đặt `\n` ở ranh giới giữa các dòng (giữa dòng 1 và 2, giữa 2 và 3, giữa 3 và 4). Không đặt `\n` ở cuối nếu không muốn có dòng trống thừa. Cạm bẫy: đếm đủ 3 dấu `\n` cho 4 dòng.
3. **Lịch mini.** Ý tưởng: mỗi "ô" chiếm một số cột cố định (ví dụ mỗi ô rộng 4 ký tự). Ở dòng tên thứ, viết `T2`, `T3`... và thêm dấu cách để mỗi nhãn lấp đầy đúng bề rộng ô. Ở dòng số ngày, viết `1`, `2`... rồi thêm dấu cách để số nằm đúng cột dưới nhãn tương ứng. Bước logic: (a) chọn bề rộng ô; (b) với ô có nhãn ngắn hơn bề rộng, bù thêm dấu cách; (c) in mỗi dòng bằng một lệnh `print`. Cạm bẫy: số một chữ số và nhãn hai ký tự chiếm bề rộng khác nhau, nên phải bù dấu cách khác nhau để thẳng cột.
