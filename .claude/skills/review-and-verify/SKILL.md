---
name: review-and-verify
description: Review độc lập các thay đổi mã nguồn, đối chiếu với rules và kế hoạch đã duyệt, tìm lỗi logic, phạm vi thừa, thiếu test và rủi ro hồi quy. Không chỉnh sửa mã nguồn.
---

# Review and Verify

## 1. Mục đích

Sử dụng Skill này sau khi mã nguồn đã được thay đổi để:

- Đối chiếu thay đổi với kế hoạch đã duyệt.
- Kiểm tra tuân thủ tài liệu quy chuẩn.
- Phát hiện lỗi logic, trường hợp biên và hồi quy.
- Kiểm tra chất lượng test.
- Đưa ra quyết định có thể chấp nhận thay đổi hay cần sửa tiếp.

Skill này là bước review độc lập, không phải bước triển khai.

## 2. Đầu vào

Cần có các đầu vào phù hợp với nhiệm vụ:

1. Tài liệu quy chuẩn của dự án.
2. Codebase hoặc phạm vi dự án.
3. Thay đổi cần review: diff, commit, pull request, danh sách tệp hoặc working tree.
4. Kế hoạch đã duyệt nếu thay đổi được triển khai từ một kế hoạch.
5. Báo cáo triển khai nếu có.

Nếu thiếu diff nhưng có working tree hoặc commit, phải tự xác định thay đổi bằng công cụ phù hợp; không hỏi lại nếu có thể tự đọc.

## 3. Giới hạn bắt buộc

Mặc định Skill này chỉ review và báo cáo.

Không được:

- Chỉnh sửa mã nguồn.
- Tạo patch hoặc diff sửa lỗi.
- Tự triển khai đề xuất.
- Tạo commit.
- Push hoặc merge.
- Thay đổi test để che giấu lỗi.

Nếu người dùng yêu cầu vừa review vừa sửa, phải hoàn thành và trình bày kết quả review trước. Việc sửa phải được thực hiện bằng một yêu cầu triển khai riêng theo Skill `implement-approved-plan`.

## 4. Thứ tự ưu tiên

1. Tài liệu quy chuẩn của dự án.
2. Yêu cầu và quyết định đã được người dùng phê duyệt.
3. Kế hoạch đã duyệt.
4. Hành vi thực tế được yêu cầu.
5. Skill này quy định phương pháp review.

Không coi code hiện tại là đúng chỉ vì nó đã được triển khai.

## 5. Nguyên tắc review

1. Review thay đổi thực tế, không chỉ review báo cáo của người triển khai.
2. Đọc đủ ngữ cảnh trước và sau đoạn thay đổi.
3. Lần theo tác động end-to-end nếu thay đổi ảnh hưởng nhiều thành phần.
4. Phân biệt lỗi có bằng chứng với suy đoán.
5. Mỗi phát hiện phải chỉ ra điều kiện xảy ra và tác động.
6. Không nêu cảnh báo chung chung không gắn với mã nguồn.
7. Ưu tiên lỗi correctness, data loss, security, compatibility và regression trước style.
8. Không yêu cầu refactor chỉ vì sở thích cá nhân.
9. Không đánh dấu đạt nếu test chưa chứng minh hành vi quan trọng.
10. Không bỏ qua thay đổi ngoài phạm vi dù code đó có vẻ hợp lý.

## 6. Mức độ phát hiện

Chỉ sử dụng các mức sau:

### Blocker

Có thể gây mất dữ liệu, lỗ hổng nghiêm trọng, hệ thống không hoạt động, migration không an toàn hoặc vi phạm trực tiếp yêu cầu bắt buộc. Không được chấp nhận thay đổi khi còn Blocker.

### Major

Sai logic, bỏ sót luồng chính, phá contract, gây hồi quy đáng kể hoặc không thực hiện đúng kế hoạch. Cần sửa trước khi chấp nhận.

### Minor

Vấn đề phạm vi hẹp, trường hợp biên ít gặp, thông báo lỗi, maintainability hoặc test chưa đầy đủ nhưng không phá luồng chính ngay lập tức.

### Suggestion

Cải tiến không bắt buộc, không ảnh hưởng tính đúng đắn của thay đổi hiện tại.

Không nâng mức độ chỉ để làm phát hiện có vẻ quan trọng hơn.

## 7. Quy trình review bắt buộc

### Bước 1: Đọc quy chuẩn và mục tiêu

Xác định:

- Quy tắc liên quan trực tiếp.
- Vấn đề cần giải quyết.
- Hành vi mong đợi.
- Phạm vi đã duyệt.
- Điều kiện hoàn thành.

### Bước 2: Lập danh sách thay đổi thực tế

Xác định:

- Tệp thêm mới.
- Tệp sửa.
- Tệp xóa.
- Cấu hình, dependency, schema hoặc migration thay đổi.
- Test được thêm, sửa, xóa hoặc skip.

Không chỉ dựa vào danh sách do người triển khai cung cấp.

### Bước 3: Đối chiếu phạm vi

Với từng thay đổi, xác định:

- Có nằm trong kế hoạch không.
- Có cần thiết để giải quyết vấn đề không.
- Có thay đổi hành vi ngoài phạm vi không.
- Có bỏ sót bước hoặc tệp trong kế hoạch không.
- Có phát sinh dependency hoặc migration chưa được duyệt không.

### Bước 4: Kiểm tra tính đúng đắn của logic

Với mỗi luồng bị thay đổi:

- Kiểm tra đầu vào.
- Kiểm tra điều kiện rẽ nhánh.
- Kiểm tra biến đổi dữ liệu.
- Kiểm tra trạng thái được tạo hoặc cập nhật.
- Kiểm tra kết quả đầu ra.
- Kiểm tra xử lý lỗi.
- Kiểm tra luồng tạo, đọc, cập nhật, xóa hoặc thu hồi liên quan.

Lần theo cả truy ngược và truy xuôi khi cần.

### Bước 5: Kiểm tra các trường hợp biên

Chỉ kiểm tra các nhóm liên quan, ví dụ:

- Null, rỗng, thiếu trường hoặc sai kiểu.
- Dữ liệu cũ và dữ liệu mới.
- Lặp lại request, retry hoặc idempotency.
- Đồng thời, race condition hoặc thứ tự sự kiện.
- Timeout, expiry hoặc mất kết nối.
- Phân quyền và trạng thái tài khoản.
- Partial failure.
- Rollback hoặc retry sau lỗi.
- Nhiều thành phần dùng chung contract.

### Bước 6: Kiểm tra bảo mật và dữ liệu

Khi liên quan, kiểm tra:

- Authentication và authorization.
- Secret, token và dữ liệu nhạy cảm.
- Input validation và injection.
- Logging dữ liệu nhạy cảm.
- Quyền truy cập dữ liệu.
- Migration, mất dữ liệu và khả năng rollback.
- Khả năng tương thích ngược.

Không đưa checklist bảo mật hình thức nếu thay đổi không liên quan.

### Bước 7: Kiểm tra test

Xác định:

- Test có tái hiện lỗi cũ trước khi fix không.
- Test có chứng minh hành vi mới không.
- Test có kiểm tra hồi quy không.
- Test có bỏ sót trường hợp biên quan trọng không.
- Assertion có đủ mạnh không.
- Có test bị xóa, skip hoặc làm yếu đi không.
- Test có phụ thuộc implementation detail quá mức không.

Nếu có kết quả chạy test, phân biệt rõ kết quả được cung cấp và kết quả tự kiểm chứng.

### Bước 8: Kiểm tra chất lượng triển khai

Kiểm tra:

- Tuân thủ convention.
- Thay đổi tối thiểu và tập trung.
- Không có code tạm, debug log hoặc dead code.
- Không lặp logic không cần thiết.
- Không tạo abstraction quá mức.
- Không thêm dependency không cần thiết.
- Error message và logging có phù hợp.

Style chỉ là phát hiện khi nó vi phạm quy chuẩn hoặc gây rủi ro bảo trì rõ ràng.

### Bước 9: Kiểm chứng từng phát hiện

Mỗi phát hiện phải có:

- Mức độ.
- Vị trí chính xác.
- Điều kiện kích hoạt.
- Hành vi hiện tại.
- Hành vi đúng.
- Tác động.
- Bằng chứng.
- Hướng sửa ở mức mô tả.

Không đưa phát hiện nếu không giải thích được cách nó xảy ra.

### Bước 10: Đưa ra quyết định review

Chỉ sử dụng một trong các kết luận:

- **Chấp nhận:** không có Blocker, Major hoặc Minor cần xử lý trước khi merge.
- **Chấp nhận với lưu ý:** không có Blocker hoặc Major; chỉ còn lưu ý không chặn.
- **Yêu cầu chỉnh sửa:** còn ít nhất một Blocker hoặc Major, hoặc nhiều Minor ảnh hưởng đáng kể.
- **Chưa đủ bằng chứng:** thiếu diff, ngữ cảnh, test hoặc dữ liệu cần thiết để kết luận.

## 8. Yêu cầu về bằng chứng

Dẫn chiếu theo định dạng:

`đường/dẫn/tệp: tên class hoặc tên hàm, dòng X-Y`

Mỗi dẫn chiếu phải giải thích:

- Đoạn thay đổi làm gì.
- Vì sao có vấn đề hoặc vì sao đúng.
- Điều kiện kích hoạt.
- Tác động có thể quan sát.

Không được:

- Chỉ nêu tên tệp.
- Suy đoán từ tên hàm.
- Khẳng định test pass khi chưa chạy hoặc chưa có kết quả đáng tin cậy.
- Báo lỗi chỉ vì code khác sở thích cá nhân.

## 9. Định dạng kết quả bắt buộc

### 1. Kết luận review

- Quyết định.
- Tóm tắt ngắn lý do.
- Số lượng phát hiện theo mức độ.

### 2. Phạm vi đã review

- Tài liệu quy chuẩn.
- Kế hoạch hoặc yêu cầu.
- Diff, commit hoặc tệp đã kiểm tra.
- Phần chưa thể kiểm tra.

### 3. Đối chiếu với kế hoạch

| Hạng mục kế hoạch | Thay đổi thực tế | Trạng thái | Ghi chú |
|---|---|---|---|

Trạng thái:

- Đúng kế hoạch.
- Thiếu.
- Sai khác.
- Ngoài phạm vi.
- Không áp dụng.

### 4. Phát hiện

Sắp xếp theo Blocker → Major → Minor → Suggestion.

Với mỗi phát hiện:

#### `[Mức độ] Tiêu đề ngắn`

- **Vị trí:** tệp, symbol và dòng.
- **Điều kiện:** khi nào xảy ra.
- **Hiện tại:** code đang làm gì.
- **Mong đợi:** hành vi đúng.
- **Tác động:** lỗi hoặc rủi ro.
- **Bằng chứng:** chuỗi logic chứng minh.
- **Hướng xử lý:** mô tả, không viết patch.

Nếu không có phát hiện, ghi rõ không phát hiện vấn đề chặn trong phạm vi đã review.

### 5. Review kiểm thử

- Test đã có.
- Hành vi được bao phủ.
- Hành vi chưa được bao phủ.
- Test bị yếu, skip hoặc thiếu nếu có.
- Kết quả chạy test đã được kiểm chứng.

### 6. Rủi ro hồi quy và tương thích

- Luồng có nguy cơ ảnh hưởng.
- Dữ liệu hoặc trạng thái cũ.
- Contract hoặc thành phần phụ thuộc.
- Migration và rollback nếu có.

### 7. Nội dung cần xử lý trước khi chấp nhận

Chỉ liệt kê các mục Blocker, Major và Minor thực sự cần xử lý trước khi merge.

### 8. Nội dung không chặn

Liệt kê Suggestion hoặc cải tiến ngoài phạm vi, tách khỏi lỗi bắt buộc.

## 10. Điểm dừng

Sau khi hoàn thành review:

- Không chỉnh sửa mã nguồn.
- Không tạo patch, commit hoặc merge.
- Không tự triển khai hướng xử lý.
- Dừng lại để người dùng quyết định bước tiếp theo.

## 11. Checklist hoàn thành

- Đã đọc quy chuẩn và mục tiêu.
- Đã review thay đổi thực tế, không chỉ báo cáo.
- Đã đối chiếu từng thay đổi với kế hoạch.
- Đã kiểm tra logic end-to-end và trường hợp biên liên quan.
- Mỗi phát hiện đều có điều kiện, tác động và bằng chứng.
- Đã đánh giá test, hồi quy, dữ liệu và tương thích.
- Không trộn suggestion với lỗi chặn.
- Không sửa mã nguồn trong giai đoạn review.
