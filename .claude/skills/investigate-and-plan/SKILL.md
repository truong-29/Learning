---
name: investigate-and-plan
description: Điều tra vấn đề trong codebase, kiểm chứng nguyên nhân gốc, đề xuất phương án và lập kế hoạch triển khai. Chỉ phân tích; không chỉnh sửa mã nguồn.
---

# Investigate and Plan

## 1. Mục đích

Sử dụng Skill này khi người dùng yêu cầu:

- Điều tra lỗi hoặc hành vi bất thường.
- Tìm nguyên nhân gốc.
- Phân tích một thay đổi cần thực hiện.
- Đề xuất phương án kỹ thuật.
- Lập kế hoạch triển khai trước khi code.

Skill này áp dụng chung cho mọi loại dự án và mọi loại vấn đề kỹ thuật.

## 2. Đầu vào bắt buộc

Trước khi bắt đầu, phải xác định được:

1. Tài liệu quy chuẩn của dự án, ví dụ `rules.md`.
2. Dự án hoặc phạm vi codebase cần phân tích.
3. Vấn đề hiện tại cần điều tra.

Nếu đường dẫn hoặc tài liệu đã được cung cấp, phải tự đọc; không hỏi lại người dùng.

## 3. Thứ tự ưu tiên

1. Tài liệu quy chuẩn của dự án là nguồn quy chuẩn chính.
2. Yêu cầu cụ thể của người dùng áp dụng trong phạm vi không xung đột với tài liệu quy chuẩn.
3. Skill này quy định phương pháp điều tra và định dạng kết quả.

Nếu yêu cầu mâu thuẫn với tài liệu quy chuẩn:

- Nêu rõ nội dung xung đột.
- Dẫn chiếu quy tắc tương ứng.
- Dừng tại phần bị xung đột.
- Không tự lựa chọn cách xử lý thay người dùng.

## 4. Giới hạn bắt buộc

Nhiệm vụ này chỉ bao gồm phân tích và lập kế hoạch.

Không được:

- Chỉnh sửa mã nguồn.
- Tạo patch hoặc diff.
- Viết mã triển khai.
- Tạo commit.
- Triển khai thử phương án.
- Tự chuyển sang giai đoạn code.

Chỉ được tạo tài liệu kế hoạch riêng nếu người dùng hoặc môi trường làm việc yêu cầu rõ ràng. Việc tạo tài liệu kế hoạch không được làm thay đổi mã nguồn sản phẩm.

## 5. Nguyên tắc điều tra

1. Đọc toàn bộ tài liệu quy chuẩn trước khi phân tích.
2. Chỉ liệt kê các quy tắc liên quan trực tiếp đến vấn đề hoặc phương án.
3. Không chỉ kiểm tra tệp được nhắc trực tiếp trong mô tả.
4. Phải lần theo đầy đủ nơi tiếp nhận, tạo, biến đổi, lưu trữ, truyền và sử dụng dữ liệu.
5. Phải xác định toàn bộ thành phần góp phần tạo ra hành vi người dùng quan sát được.
6. Nếu hành vi đi qua nhiều module, service, frontend, backend, worker hoặc hệ thống ngoài, phải kiểm tra các ranh giới liên quan.
7. Mọi kết luận phải dựa trên bằng chứng có thể kiểm chứng từ mã nguồn, cấu hình, dữ liệu, log hoặc kết quả tái hiện.
8. Khi chưa đủ bằng chứng, phải ghi rõ đó là giả thuyết.
9. Không được chọn giải pháp chỉ vì dễ triển khai.
10. Chỉ đề xuất thay đổi liên quan trực tiếp đến nguyên nhân; không mở rộng phạm vi hoặc tái cấu trúc không cần thiết.

## 6. Tiêu chuẩn xác nhận nguyên nhân

Phải phân biệt rõ các trạng thái sau:

### Có khả năng xảy ra

Mã nguồn hoặc cấu hình cho thấy tình huống có thể gây ra vấn đề, nhưng chưa có bằng chứng rằng đó là nguyên nhân của sự cố hiện tại.

### Khả năng cao

Có nhiều bằng chứng phù hợp, nhưng vẫn còn thông tin chưa kiểm tra hoặc nguyên nhân khác chưa được loại trừ.

### Đã xác nhận

Có đủ bằng chứng chứng minh đầy đủ chuỗi:

`Điều kiện kích hoạt → Luồng thực thi → Điểm sai lệch → Hành vi quan sát được`

### Chưa đủ bằng chứng

Thiếu cấu hình thực tế, dữ liệu chạy, log, trạng thái hệ thống, bước tái hiện hoặc mắt xích cần thiết trong chuỗi nguyên nhân.

### Đã loại trừ

Bằng chứng cho thấy điều kiện cần không tồn tại hoặc luồng thực tế không thể tạo ra hành vi đang điều tra.

Chỉ được sử dụng năm trạng thái trên. Không sử dụng phần trăm như `90%`, `99%` hoặc `100%`.

Việc tìm thấy một đoạn mã có khả năng tạo lỗi không đồng nghĩa đoạn mã đó là nguyên nhân của sự cố hiện tại.

Nếu nhiều nhánh cùng tạo ra một kết quả hoặc một loại lỗi, phải:

- Liệt kê từng nhánh.
- Xác định điều kiện kích hoạt của từng nhánh.
- Chỉ ra dấu hiệu phân biệt.
- Kiểm chứng từng nhánh độc lập.
- Không gom tất cả thành một nguyên nhân.

## 7. Quy trình bắt buộc

### Bước 1: Chuẩn hóa vấn đề

Làm rõ:

- Hành vi hiện tại.
- Hành vi mong đợi.
- Điều kiện xuất hiện.
- Tần suất nếu xác định được.
- Phạm vi có khả năng bị ảnh hưởng.
- Thành phần hệ thống có khả năng liên quan.

Phân loại thông tin thành:

- Người dùng đã cung cấp.
- Đã xác nhận từ hệ thống.
- Giả định cần kiểm tra.

Không tự bổ sung giả định mà không ghi rõ.

### Bước 2: Xác định ranh giới và điểm bắt đầu

Xác định:

- Thành phần tiếp nhận yêu cầu.
- Thành phần xử lý.
- Thành phần lưu trữ hoặc truyền dữ liệu.
- Thành phần tạo ra hành vi quan sát được.

Điểm bắt đầu có thể là endpoint, controller, worker, consumer, scheduler, event handler, workflow node, service, UI action, background process, callback hoặc webhook.

Với điểm bắt đầu, ghi rõ:

- Đường dẫn tệp.
- Class, hàm hoặc symbol.
- Dữ liệu đầu vào.
- Thành phần gọi đến.
- Điều kiện kích hoạt.

### Bước 3: Lần theo luồng thực thi và dữ liệu

Lần theo từ điểm bắt đầu đến hành vi lỗi.

Với mỗi bước quan trọng, xác định:

- Tệp và symbol đang thực thi.
- Thành phần gọi đến nó.
- Dữ liệu đầu vào.
- Trạng thái hoặc cấu hình được sử dụng.
- Điều kiện rẽ nhánh.
- Logic biến đổi.
- Dữ liệu đầu ra.
- Thành phần tiếp theo nhận dữ liệu.
- Lỗi hoặc trường hợp biên có thể phát sinh.

Phải kiểm tra cả hai chiều:

- **Truy ngược:** dữ liệu, trạng thái hoặc cấu hình được tạo từ đâu.
- **Truy xuôi:** dữ liệu được truyền đến đâu và được sử dụng như thế nào.

Không dừng tại nơi chỉ phát hiện hoặc trả về lỗi. Phải tìm nơi bắt đầu tạo ra dữ liệu, trạng thái hoặc điều kiện sai.

### Bước 4: Kiểm tra các nhánh tạo cùng triệu chứng

Tìm tất cả nhánh có thể tạo ra cùng hành vi hoặc cùng loại lỗi.

Với từng nhánh, ghi rõ:

- Điều kiện kích hoạt.
- Vị trí trong mã nguồn.
- Kết quả tạo ra.
- Dấu hiệu phân biệt.
- Trạng thái kiểm chứng.

### Bước 5: Xây dựng và kiểm chứng giả thuyết

Với mỗi giả thuyết, trình bày:

- Mô tả.
- Điều kiện cần.
- Bằng chứng ủng hộ.
- Bằng chứng phản bác hoặc điểm chưa khớp.
- Thông tin còn thiếu.
- Cách kiểm chứng.
- Kết quả kiểm chứng.
- Trạng thái kết luận.

Không kết luận theo giả thuyết đầu tiên tìm thấy.

### Bước 6: Xác định nguyên nhân gốc

Phân biệt:

- **Triệu chứng:** biểu hiện quan sát được.
- **Nguyên nhân trực tiếp:** logic hoặc trạng thái trực tiếp tạo ra triệu chứng.
- **Nguyên nhân gốc:** lý do khiến hệ thống đi vào logic hoặc trạng thái sai.
- **Yếu tố góp phần:** điều kiện làm vấn đề dễ xuất hiện hoặc khó phát hiện hơn nhưng không phải nguyên nhân chính.

Kết luận phải trả lời:

1. Sai lệch bắt đầu tại đâu?
2. Điều kiện nào kích hoạt?
3. Dữ liệu, trạng thái hoặc cấu hình nào liên quan?
4. Vì sao logic hiện tại xử lý không đúng?
5. Sai lệch được truyền qua các thành phần như thế nào?
6. Vì sao người dùng quan sát được hành vi đó?
7. Trường hợp nào bị ảnh hưởng?
8. Trường hợp nào không bị ảnh hưởng?
9. Bằng chứng nào xác nhận kết luận?
10. Phần nào vẫn chưa đủ bằng chứng?

Nếu chưa đủ bằng chứng, phải nói rõ và không tạo kết luận chắc chắn.

### Bước 7: Đề xuất phương án

Chỉ đề xuất sau khi hoàn thành phân tích nguyên nhân.

Với mỗi phương án, nêu:

- Nguyên nhân được xử lý.
- Nguyên lý.
- Tệp và khu vực logic dự kiến thay đổi.
- Luồng liên quan bị tác động.
- Ưu điểm.
- Nhược điểm.
- Rủi ro.
- Ảnh hưởng đến chức năng hiện có.
- Khả năng tương thích với dữ liệu hoặc trạng thái hiện tại.
- Trường hợp biên.
- Cách kiểm thử.
- Điều kiện cần từ thành phần khác.

Không được đề xuất giải pháp chỉ xử lý triệu chứng mà bỏ qua nguyên nhân gốc, trừ khi ghi rõ đó là giải pháp tạm thời.

Nếu có nhiều phương án:

1. So sánh từng phương án.
2. Phân biệt phương án tạm thời và lâu dài nếu có.
3. Chọn một phương án khuyến nghị.
4. Giải thích lý do lựa chọn.

### Bước 8: Kiểm tra tác động

Kiểm tra phương án đối với các luồng thực sự liên quan:

- Tạo dữ liệu.
- Đọc hoặc sử dụng dữ liệu.
- Cập nhật.
- Xóa hoặc thu hồi.
- Xử lý lỗi.
- Tác vụ nền hoặc bất đồng bộ.
- Dữ liệu hoặc trạng thái đang tồn tại.
- Khả năng tương thích ngược.
- Thành phần phụ thuộc.

Nếu cần chuyển đổi dữ liệu hoặc trạng thái, phải có phương án migration hoặc tương thích chuyển tiếp.

### Bước 9: Lập kế hoạch triển khai

Mỗi bước kế hoạch phải có:

- Mục tiêu.
- Tệp, class hoặc hàm dự kiến tác động.
- Logic cần thay đổi ở mức mô tả.
- Lý do.
- Phụ thuộc.
- Tác động đến luồng hiện tại.
- Rủi ro.
- Cách kiểm chứng.
- Điều kiện hoàn thành.

Kế hoạch phải đủ chi tiết để lập trình viên khác triển khai mà không phải điều tra lại từ đầu.

Không viết mã nguồn, patch, diff hoặc pseudocode chi tiết có thể dùng trực tiếp như mã triển khai.

## 8. Yêu cầu về bằng chứng

Mọi phát hiện quan trọng phải dẫn chiếu theo định dạng:

`đường/dẫn/tệp: tên class hoặc tên hàm`

Nếu có số dòng, ghi thêm khoảng dòng.

Mỗi dẫn chiếu phải giải thích:

- Đoạn mã đang làm gì.
- Vì sao liên quan đến vấn đề.
- Nó chứng minh hoặc bác bỏ nhận định nào.
- Nó chỉ chứng minh khả năng xảy ra hay chứng minh sự cố thực tế.

Không được:

- Chỉ liệt kê tên tệp.
- Suy đoán hành vi từ tên hàm, biến hoặc class khi chưa đọc logic.
- Coi giá trị mặc định là giá trị thực tế khi chưa kiểm tra cấu hình chạy.

Nếu dùng cấu hình làm bằng chứng, ghi rõ:

- Tệp hoặc nguồn cấu hình.
- Tên cấu hình.
- Giá trị thực tế nếu đọc được.
- Giá trị mặc định nếu có.
- Thành phần sử dụng.

## 9. Định dạng kết quả bắt buộc

### 1. Tóm tắt vấn đề

- Hành vi hiện tại.
- Hành vi mong đợi.
- Điều kiện xuất hiện.
- Phạm vi ảnh hưởng.
- Thông tin đã xác nhận.
- Thông tin đang là giả định.

### 2. Quy tắc liên quan trong tài liệu quy chuẩn

Chỉ liệt kê quy tắc có tác động trực tiếp, kèm ảnh hưởng và xung đột nếu có.

### 3. Thành phần và phạm vi điều tra

- Module hoặc thành phần liên quan.
- Điểm bắt đầu.
- Điểm kết thúc.
- Ranh giới giữa các thành phần.
- Lý do cần kiểm tra từng thành phần.

### 4. Luồng thực thi hiện tại

Trình bày:

`Đầu vào → Điểm tiếp nhận → Xử lý → Biến đổi dữ liệu → Lưu hoặc truyền tiếp → Xử lý kết quả → Hành vi quan sát được`

Kèm tệp và symbol tại từng bước quan trọng.

### 5. Các nhánh có thể tạo cùng triệu chứng

| Nhánh | Điều kiện kích hoạt | Kết quả | Cách phân biệt | Trạng thái kiểm chứng |
|---|---|---|---|---|

### 6. Các giả thuyết đã kiểm tra

| Giả thuyết | Bằng chứng ủng hộ | Bằng chứng phản bác | Thông tin còn thiếu | Kết quả |
|---|---|---|---|---|

### 7. Nguyên nhân gốc

- Triệu chứng.
- Nguyên nhân trực tiếp.
- Nguyên nhân gốc.
- Yếu tố góp phần.
- Điều kiện kích hoạt.
- Chuỗi bằng chứng.
- Phạm vi ảnh hưởng.
- Trạng thái kết luận.
- Nội dung chưa đủ bằng chứng.

### 8. Phương án giải quyết

Với mỗi phương án, trình bày nguyên nhân được xử lý, nguyên lý, vị trí tác động, ưu nhược điểm, rủi ro, tương thích, trường hợp biên và cách kiểm thử.

Nêu rõ phương án khuyến nghị và lý do.

### 9. Kế hoạch triển khai

Trình bày từng bước theo cấu trúc bắt buộc nhưng không viết mã.

### 10. Kế hoạch kiểm thử

Bao gồm:

- Tái hiện vấn đề hiện tại.
- Trường hợp hoạt động bình thường.
- Dữ liệu thiếu hoặc không hợp lệ.
- Trường hợp biên.
- Nhiều nhánh tạo cùng triệu chứng.
- Kiểm thử tích hợp.
- Kiểm thử hồi quy.
- Dữ liệu hoặc trạng thái cũ nếu có thay đổi cấu trúc.

### 11. Nội dung cần xác nhận

Chỉ hỏi quyết định không thể tự xác định từ mã nguồn, cấu hình hoặc tài liệu.

Với mỗi nội dung, nêu lý do cần hỏi, các lựa chọn, ảnh hưởng và phương án khuyến nghị nếu đủ cơ sở.

## 10. Điểm dừng

Sau khi hoàn thành phân tích và kế hoạch:

- Dừng lại để người dùng review.
- Không chỉnh sửa mã nguồn.
- Không tạo patch, diff hoặc commit.
- Không triển khai thử.
- Không tự chuyển sang giai đoạn code.
- Chỉ được code khi người dùng xác nhận bằng một yêu cầu mới.

## 11. Checklist hoàn thành

Trước khi trả kết quả, tự kiểm tra:

- Đã đọc toàn bộ tài liệu quy chuẩn.
- Đã lần theo luồng end-to-end.
- Đã kiểm tra các nhánh tạo cùng triệu chứng.
- Không biến khả năng thành nguyên nhân đã xác nhận.
- Mỗi kết luận quan trọng đều có bằng chứng.
- Phương án xử lý đúng nguyên nhân, không chỉ xử lý triệu chứng.
- Đã đánh giá tác động và tương thích.
- Kế hoạch đủ chi tiết nhưng không chứa code.
- Đã dừng trước giai đoạn triển khai.
