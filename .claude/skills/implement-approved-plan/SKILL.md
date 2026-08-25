---
name: implement-approved-plan
description: Triển khai đúng kế hoạch đã được người dùng phê duyệt, sửa mã nguồn trong phạm vi khóa, kiểm thử và báo cáo thay đổi.
---

# Implement Approved Plan

## 1. Mục đích

Sử dụng Skill này khi người dùng đã xem xét kế hoạch và đưa ra yêu cầu mới cho phép triển khai mã nguồn.

Skill này không dùng để tự điều tra lại từ đầu hoặc tự thiết kế một phương án khác.

## 2. Điều kiện kích hoạt bắt buộc

Chỉ được triển khai khi có đầy đủ:

1. Tài liệu quy chuẩn của dự án.
2. Dự án hoặc phạm vi codebase cần sửa.
3. Kế hoạch triển khai đã được phê duyệt.
4. Yêu cầu rõ ràng của người dùng cho phép code hoặc triển khai.

Không được coi các câu như “ổn”, “xem tiếp”, “phân tích thêm” hoặc sự im lặng là quyền triển khai.

Nếu thiếu kế hoạch đã duyệt hoặc thiếu quyền triển khai rõ ràng:

- Không sửa mã nguồn.
- Nêu điều kiện còn thiếu.
- Dừng lại.

## 3. Thứ tự ưu tiên

1. Tài liệu quy chuẩn của dự án.
2. Quyết định và phạm vi người dùng đã phê duyệt.
3. Kế hoạch triển khai đã duyệt.
4. Skill này quy định phương pháp thực hiện.

Nếu kế hoạch mâu thuẫn với tài liệu quy chuẩn:

- Không tự ý triển khai phần xung đột.
- Dẫn chiếu nội dung xung đột.
- Báo cáo để người dùng quyết định.

## 4. Khóa phạm vi

Chỉ được thay đổi những gì cần thiết để thực hiện kế hoạch đã duyệt.

Không được:

- Tự thêm tính năng ngoài kế hoạch.
- Tự thay đổi kiến trúc đã được duyệt.
- Refactor diện rộng chỉ để “làm code đẹp hơn”.
- Đổi API, schema, contract hoặc hành vi không liên quan.
- Sửa các lỗi khác tình cờ phát hiện nếu chúng không chặn triển khai.
- Xóa dữ liệu, tạo migration phá hủy hoặc thay đổi tương thích mà chưa được phê duyệt.

Nếu phát hiện vấn đề ngoài phạm vi:

- Ghi nhận riêng.
- Không sửa trong nhiệm vụ hiện tại.

## 5. Xử lý khi codebase khác với kế hoạch

Trước khi sửa, phải kiểm tra lại mã nguồn hiện tại.

Nếu codebase chỉ khác nhỏ và không làm thay đổi mục tiêu, hành vi, phạm vi hoặc rủi ro của kế hoạch:

- Có thể điều chỉnh chi tiết triển khai tối thiểu.
- Phải ghi rõ điều chỉnh trong báo cáo.

Nếu khác biệt làm thay đổi một trong các nội dung sau:

- Nguyên nhân gốc.
- Kiến trúc giải pháp.
- Contract.
- Dữ liệu hoặc migration.
- Phạm vi tệp.
- Rủi ro.
- Tác động đến hệ thống khác.

thì phải dừng và yêu cầu cập nhật hoặc phê duyệt lại kế hoạch. Không tự quyết định.

## 6. Quy trình triển khai bắt buộc

### Bước 1: Đọc và đối chiếu đầu vào

Đọc đầy đủ:

- Tài liệu quy chuẩn.
- Kế hoạch đã duyệt.
- Phản hồi hoặc điều chỉnh của người dùng.
- Các tệp mã nguồn dự kiến tác động.

Tóm tắt nội bộ:

- Mục tiêu đã duyệt.
- Phạm vi được phép.
- Hành vi phải giữ nguyên.
- Điều kiện hoàn thành.

### Bước 2: Xác minh lại điểm sửa

Với từng bước kế hoạch:

- Xác nhận tệp, class, hàm hoặc symbol vẫn tồn tại.
- Xác nhận luồng gọi và dữ liệu phù hợp với phân tích.
- Xác nhận không có thay đổi mới làm kế hoạch lỗi thời.
- Xác định test hiện có liên quan.

Không bắt đầu sửa nếu điểm sửa chưa được xác minh.

### Bước 3: Lập bản đồ thay đổi

Trước khi chỉnh sửa, xác định:

- Tệp cần sửa.
- Tệp cần thêm nếu kế hoạch cho phép.
- Test cần sửa hoặc bổ sung.
- Cấu hình, schema hoặc migration nếu đã được duyệt.
- Thứ tự triển khai để tránh trạng thái trung gian không nhất quán.

Không mở rộng bản đồ thay đổi ngoài phạm vi đã duyệt.

### Bước 4: Triển khai theo từng bước nhỏ

Thực hiện đúng thứ tự kế hoạch.

Với mỗi thay đổi:

- Giữ thay đổi nhỏ và tập trung.
- Tuân thủ convention hiện có.
- Không sao chép logic nếu dự án đã có abstraction phù hợp.
- Không tạo abstraction mới nếu không cần thiết.
- Bảo toàn hành vi không liên quan.
- Xử lý lỗi và trường hợp biên đã nêu trong kế hoạch.
- Cập nhật các luồng tạo, đọc, cập nhật, xóa hoặc thu hồi có liên quan.

### Bước 5: Kiểm tra tương thích và dữ liệu hiện tại

Nếu thay đổi ảnh hưởng đến dữ liệu, trạng thái hoặc contract:

- Thực hiện đúng phương án migration đã duyệt.
- Kiểm tra dữ liệu cũ.
- Kiểm tra khả năng rollback nếu kế hoạch yêu cầu.
- Không tạo migration phá hủy ngoài phê duyệt.
- Không giả định môi trường trống.

### Bước 6: Viết hoặc cập nhật kiểm thử

Thực hiện các kiểm thử trong kế hoạch, bao gồm khi liên quan:

- Tái hiện lỗi cũ.
- Trường hợp hoạt động bình thường.
- Dữ liệu thiếu hoặc không hợp lệ.
- Trường hợp biên.
- Tích hợp giữa các thành phần.
- Hồi quy cho hành vi hiện có.
- Dữ liệu hoặc trạng thái cũ.

Test phải kiểm tra hành vi, không chỉ kiểm tra implementation detail.

### Bước 7: Chạy kiểm tra

Ưu tiên chạy kiểm tra hẹp trước, sau đó mở rộng:

1. Test trực tiếp liên quan.
2. Test của module.
3. Static analysis, type check, lint hoặc format theo quy chuẩn dự án.
4. Test tích hợp hoặc toàn bộ test suite nếu khả thi và cần thiết.

Nếu không thể chạy một kiểm tra:

- Không được nói rằng kiểm tra đã thành công.
- Ghi rõ lệnh chưa chạy hoặc đã thất bại.
- Nêu nguyên nhân.
- Nêu rủi ro còn lại.

### Bước 8: Tự review thay đổi

Trước khi kết thúc, kiểm tra:

- Thay đổi có đúng kế hoạch không.
- Có sửa ngoài phạm vi không.
- Có bỏ sót luồng liên quan không.
- Có làm thay đổi contract hoặc hành vi ngoài ý muốn không.
- Có để lại mã tạm, debug log, secret hoặc dữ liệu nhạy cảm không.
- Có xử lý trường hợp lỗi và tương thích không.
- Test có thực sự bắt được lỗi cũ không.

### Bước 9: Báo cáo

Báo cáo trung thực những gì đã thực hiện, không phóng đại mức độ hoàn thành.

## 7. Quy tắc chỉnh sửa

- Ưu tiên thay đổi tối thiểu nhưng đầy đủ.
- Không viết lại toàn bộ tệp nếu chỉ cần sửa một khu vực.
- Không thay đổi format hàng loạt ngoài phạm vi.
- Không đổi tên public symbol nếu kế hoạch không yêu cầu.
- Không thêm dependency mới nếu chưa được duyệt hoặc không thực sự cần thiết.
- Không ghi secret, token hoặc dữ liệu thật vào mã nguồn, test hoặc log.
- Không làm suy yếu validation, authentication, authorization hoặc error handling để test “chạy qua”.
- Không bỏ qua test thất bại bằng cách xóa, skip hoặc nới lỏng assertion nếu không có lý do được phê duyệt.

## 8. Định dạng báo cáo bắt buộc

### 1. Kế hoạch đã triển khai

- Mục tiêu.
- Phạm vi đã duyệt.
- Điều chỉnh được người dùng yêu cầu thêm nếu có.

### 2. Các tệp đã thay đổi

Với mỗi tệp:

- Đường dẫn.
- Class, hàm hoặc khu vực thay đổi.
- Nội dung thay đổi.
- Lý do.

### 3. Chi tiết triển khai theo từng bước

Đối chiếu từng bước trong kế hoạch với trạng thái:

- Hoàn thành.
- Hoàn thành có điều chỉnh.
- Chưa thực hiện.
- Bị chặn.

### 4. Sai khác so với kế hoạch

Với mỗi sai khác:

- Nội dung.
- Lý do.
- Có làm thay đổi hành vi hoặc rủi ro không.

Nếu không có, ghi rõ không có.

### 5. Kiểm thử và kiểm tra đã chạy

| Kiểm tra | Lệnh hoặc phạm vi | Kết quả | Ghi chú |
|---|---|---|---|

Không ghi “pass” nếu không thực sự chạy.

### 6. Tác động và tương thích

- Hành vi được sửa.
- Hành vi được giữ nguyên.
- Ảnh hưởng đến dữ liệu, contract hoặc thành phần khác.
- Migration hoặc tương thích chuyển tiếp nếu có.

### 7. Rủi ro và phần còn lại

- Rủi ro chưa kiểm chứng.
- Test chưa chạy được.
- Vấn đề ngoài phạm vi đã phát hiện.
- Việc cần thực hiện ở môi trường triển khai nếu có.

### 8. Trạng thái cuối cùng

Chỉ sử dụng một trạng thái:

- Hoàn thành và đã kiểm chứng.
- Hoàn thành nhưng còn kiểm chứng thủ công.
- Hoàn thành một phần.
- Bị chặn.

## 9. Điểm dừng

Sau khi hoàn thành phạm vi đã duyệt:

- Không tự mở rộng sang yêu cầu khác.
- Không tự sửa các vấn đề ngoài phạm vi.
- Không tự tạo commit hoặc push nếu người dùng chưa yêu cầu.
- Báo cáo kết quả và dừng lại.

## 10. Checklist hoàn thành

- Có quyền triển khai rõ ràng.
- Đã đọc tài liệu quy chuẩn và kế hoạch được duyệt.
- Mọi thay đổi đều nằm trong phạm vi.
- Đã kiểm tra codebase hiện tại trước khi sửa.
- Đã xử lý các luồng liên quan trong kế hoạch.
- Đã viết hoặc cập nhật test cần thiết.
- Không tuyên bố đã chạy kiểm tra khi chưa chạy.
- Không còn mã tạm, secret hoặc debug artifact.
- Đã báo cáo mọi sai khác, rủi ro và phần chưa kiểm chứng.
