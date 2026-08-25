---
name: inspect-and-answer
description: Đọc mã nguồn, cấu hình, log, dữ liệu và runtime để trả lời chính xác câu hỏi kỹ thuật dựa trên bằng chứng. Chỉ kiểm tra, trace, đối chiếu và giải thích; không tự lập kế hoạch triển khai hoặc chỉnh sửa mã nguồn.
---

# Inspect and Answer

## 1. Mục đích

Sử dụng Skill này khi người dùng muốn hỏi về trạng thái, hành vi hoặc logic hiện tại của hệ thống và cần câu trả lời dựa trên codebase hoặc runtime thực tế.

Ví dụ:

- "Đoạn này hiện tại chạy như thế nào?"
- "API này lấy dữ liệu từ đâu?"
- "Tại sao request này trả 401?"
- "Kiểm tra log Docker xem nó đang dừng ở đâu."
- "Frontend đang gọi endpoint nào?"
- "Module này có sử dụng Redis không?"
- "Hai implementation này khác nhau ở đâu?"
- "Config thực tế đang lấy từ `.env` hay Config Server?"
- "Cái này có phải do auth không?"
- "Thư viện này và project hiện tại đang dùng khác nhau thế nào?"

Mục tiêu:

`Câu hỏi → Đọc bằng chứng → Trace đủ phạm vi → Trả lời chính xác → Dừng`

Skill này KHÔNG mặc định biến câu hỏi thành:

`Điều tra root cause toàn diện → Đề xuất giải pháp → Lập Final Plan → Sửa code`

Nếu người dùng yêu cầu rõ ràng tìm nguyên nhân gốc và lập kế hoạch sửa, sử dụng `investigate-and-plan`.

---

## 2. Khi nào sử dụng

Sử dụng khi mục tiêu chính là:

- Tìm hiểu logic hiện tại.
- Kiểm tra trạng thái hiện tại.
- Kiểm tra một giả định.
- Giải thích lỗi hoặc log.
- Xác định component, API, service hoặc dữ liệu đang được sử dụng.
- Đối chiếu nhiều implementation.
- Xác minh một hành vi có tồn tại hay không.
- Kiểm tra cấu hình runtime.
- Kiểm tra Docker/container/process/log.
- Trace một request hoặc dữ liệu.
- Trả lời câu hỏi kiến trúc dựa trên implementation hiện tại.
- Kiểm tra một phát biểu hoặc tài liệu có đúng với source hiện tại hay không.

Không sử dụng Skill này làm Skill chính khi người dùng yêu cầu:

- Điều tra root cause đầy đủ.
- Đề xuất phương án sửa.
- Lập Final Plan.
- Triển khai code.
- Review code hoặc diff đã triển khai.

Các nhiệm vụ đó tương ứng với:

- `investigate-and-plan`
- `implement-approved-plan`
- `review-and-verify`

---

## 3. Đầu vào

Cần xác định các đầu vào phù hợp:

1. Tài liệu quy chuẩn của dự án nếu có.
2. Project hoặc phạm vi codebase cần kiểm tra.
3. Một hoặc nhiều câu hỏi cần trả lời.
4. Log, lỗi, request, screenshot hoặc runtime evidence nếu người dùng cung cấp.
5. Các project hoặc library liên quan nếu câu hỏi đi qua nhiều hệ thống.

Nếu đường dẫn, project, log hoặc tài liệu đã được cung cấp:

- Phải tự đọc.
- Không hỏi lại người dùng thông tin có thể tự xác định.

Không bắt buộc người dùng phải cung cấp:

- Execution plan.
- Root-cause hypothesis.
- Danh sách tệp cần đọc.
- Tên chính xác của function.
- Tên container nếu có thể tự tìm.
- Thông tin có thể xác định từ codebase hoặc runtime.

---

## 4. Thứ tự ưu tiên

1. Global rules hoặc tài liệu quy chuẩn của workspace.
2. Project-specific rules áp dụng cho project hiện tại.
3. Yêu cầu cụ thể của người dùng.
4. Source code và runtime behavior thực tế.
5. Tài liệu kiến trúc hoặc knowledge document.
6. Skill này quy định phương pháp kiểm tra và cách trả lời.

Nếu documentation khác code/runtime:

- Không tự coi documentation đúng.
- Không tự coi code đúng.
- Chỉ ra discrepancy.
- Xác định thứ thực sự quyết định runtime behavior.
- Ghi rõ trạng thái kết luận.

Nếu yêu cầu người dùng xung đột rules:

- Nêu nội dung xung đột.
- Dẫn chiếu quy tắc.
- Không thực hiện phần bị cấm.

---

## 5. Giới hạn bắt buộc

Skill này là nhiệm vụ kiểm tra và hỏi đáp.

Mặc định KHÔNG được:

- Chỉnh sửa mã nguồn.
- Chỉnh sửa config.
- Chỉnh sửa database.
- Tạo patch.
- Tạo diff sửa lỗi.
- Tạo migration.
- Tạo commit.
- Push.
- Merge.
- Build hoặc rollout hệ thống.
- Restart/recreate container.
- Tự triển khai phương án.
- Tự tạo Final Plan.
- Tự chuyển sang Skill khác.
- Tự refactor code.
- Tự "sửa luôn" lỗi phát hiện được.

Được phép sử dụng thao tác read-only khi cần:

- Đọc source.
- Search source.
- Đọc file cấu hình.
- Đọc log.
- Xem Docker logs.
- Inspect container.
- Kiểm tra environment ở dạng an toàn.
- Query database read-only.
- Kiểm tra process/runtime state.
- Gọi diagnostic API không làm thay đổi dữ liệu.
- Chạy static inspection.

Nếu thao tác có khả năng thay đổi trạng thái:

- Không thực hiện mặc định.
- Nêu rõ cần nhiệm vụ hoặc quyền triển khai khác.

---

## 6. Ranh giới với `investigate-and-plan`

### `inspect-and-answer`

Mục tiêu:

> Trả lời câu hỏi hiện tại.

Chỉ trace đến mức cần thiết để trả lời chính xác.

Ví dụ người dùng hỏi:

> "401 này được ném ở đâu?"

Chỉ cần xác định:

`request → dependency → function → condition → 401`

Không bắt buộc tiếp tục:

`→ nguyên nhân kiến trúc → các phương án → Final Plan`

### `investigate-and-plan`

Mục tiêu:

> Tìm nguyên nhân gốc đầy đủ và lập kế hoạch sửa.

Phải:

- kiểm tra nhiều hypothesis;
- loại trừ các nhánh;
- xác định root cause;
- đánh giá tác động;
- so sánh phương án;
- lập Final Plan.

Không được tự chuyển từ `inspect-and-answer` sang `investigate-and-plan`.

Nếu câu trả lời cho thấy cần điều tra sâu hơn:

- Nêu ngắn gọn rằng cần một nhiệm vụ `investigate-and-plan`.
- Không tự thực hiện.
- Dừng sau khi trả lời câu hỏi hiện tại.

---

## 7. Nguyên tắc kiểm tra

1. Phải đọc nội dung thực tế của các tệp liên quan trước khi kết luận.

2. Không suy đoán behavior chỉ dựa trên:

   - Tên file.
   - Tên folder.
   - Tên class.
   - Tên function.
   - Tên variable.
   - Tên endpoint.
   - Tên config.
   - HTTP status.
   - Error message.
   - Convention phổ biến của framework.

3. Với mỗi câu hỏi, phải xác định phạm vi cần đọc.

4. Chỉ trace sâu đến mức cần thiết để câu trả lời đúng.

5. Không dừng ở wrapper nếu logic quyết định nằm ở dependency/service phía dưới.

6. Không trace toàn hệ thống nếu câu hỏi chỉ liên quan phạm vi nhỏ.

7. Nếu dữ liệu đi qua nhiều thành phần, phải kiểm tra đủ boundary liên quan.

8. Phải phân biệt:

   - Source behavior.
   - Runtime state.
   - Documentation/intended behavior.
   - Suy luận.

9. Không coi default config là runtime config.

10. Không coi unit test là bằng chứng runtime nếu câu hỏi hỏi trạng thái hệ thống đang chạy.

11. Không coi HTTP 200 là bằng chứng toàn bộ business flow thành công.

12. Không coi HTTP 401/403/500/503 tự nó chứng minh nguyên nhân.

13. Nếu một function có nhiều caller, phải xác định caller thực sự liên quan đến câu hỏi.

14. Nếu endpoint có nhiều dependency, phải xác định dependency thực sự quyết định behavior.

15. Nếu nhiều project tham gia, phải kiểm tra đúng boundary giữa chúng.

16. Không mở rộng thành architecture review toàn hệ thống nếu câu hỏi không yêu cầu.

17. Nếu phát hiện vấn đề ngoài câu hỏi:

   - Chỉ nêu nếu ảnh hưởng trực tiếp đến tính đúng đắn của câu trả lời.
   - Không tự lập kế hoạch sửa.

---

## 8. Trạng thái kết luận

Mỗi nhận định quan trọng phải thuộc một trong ba trạng thái:

### Đã xác nhận

Có bằng chứng trực tiếp từ:

- Source code.
- Runtime state.
- Config thực tế.
- Database.
- Log.
- API response.
- Tài liệu authoritative.

Bằng chứng trực tiếp hỗ trợ nhận định.

### Suy luận

Không có một evidence duy nhất nói trực tiếp điều đó nhưng kết luận được suy ra hợp lý từ nhiều bằng chứng đã xác nhận.

Phải nói rõ đây là suy luận.

### Chưa xác định

Evidence hiện tại chưa đủ để kết luận.

Không được biến `Chưa xác định` thành phỏng đoán.

Không sử dụng phần trăm như:

- 90%
- 95%
- 99%
- 100%

để thay thế trạng thái bằng chứng.

---

## 9. Quy trình bắt buộc

### Bước 1: Chuẩn hóa câu hỏi

Tách câu hỏi người dùng thành các câu hỏi cụ thể.

Ví dụ:

> "SSO xong load rồi đứng im trang login, kiểm tra Docker xem sao."

Có thể cần trả lời:

1. Browser đã callback thành công chưa?
2. Backend đã tạo session/cookie chưa?
3. Frontend gọi API nào sau redirect?
4. Request nào đang trả lỗi?
5. Container nào có log liên quan?
6. UI đứng ở frontend guard hay backend?

Không tự biến thành:

> "Thiết kế lại toàn bộ Authentication."

Nếu có nhiều câu hỏi, giữ đúng thứ tự người dùng đưa ra.

---

### Bước 2: Xác định evidence cần thiết

Xác định loại evidence cần để trả lời:

- Source.
- Config.
- Runtime log.
- Container state.
- Database.
- Request/response.
- Frontend caller.
- Backend handler.
- Worker.
- Queue.
- External service.
- Documentation.

Không đọc mọi thứ nếu không liên quan.

---

### Bước 3: Xác định điểm bắt đầu

Điểm bắt đầu có thể là:

- UI component.
- API request.
- Endpoint.
- Log line.
- Error.
- Function.
- Queue message.
- Worker consumer.
- Config field.
- Database record.
- Startup lifecycle.
- Callback.
- Webhook.

Ghi nhận khi cần:

- Tệp.
- Symbol.
- Input.
- Caller.
- Runtime condition.

---

### Bước 4: Trace logic đủ phạm vi

Nếu câu hỏi liên quan flow hoặc dữ liệu, kiểm tra khi cần:

- Nơi tiếp nhận đầu vào.
- Nơi tạo dữ liệu.
- Nơi biến đổi.
- Nơi lưu trữ.
- Nơi truyền.
- Nơi gọi service.
- Nơi sử dụng kết quả.
- Điều kiện rẽ nhánh.
- Error handling.
- Retry/fallback.
- Authentication/authorization dependency.

Trace theo hai chiều khi cần:

- Truy ngược: giá trị hoặc trạng thái này đến từ đâu?
- Truy xuôi: sau đó nó được truyền và sử dụng ở đâu?

Không trace tiếp nếu đã đủ evidence để trả lời.

---

### Bước 5: Kiểm tra runtime khi câu hỏi phụ thuộc runtime

Nếu câu hỏi là:

- "Container hiện dùng config gì?"
- "Tại sao hiện tại trả 503?"
- "Docker đang lỗi gì?"
- "Account này role gì?"
- "Request thật đang gọi endpoint nào?"

thì source một mình không đủ.

Phải kiểm tra runtime nếu môi trường cho phép.

Ví dụ:

- Docker logs.
- Container environment.
- Process command.
- Runtime route.
- Database read-only.
- HTTP request.
- Startup log.

Nếu không kiểm tra được:

- Ghi rõ runtime chưa được kiểm chứng.
- Không biến source default thành runtime fact.

---

### Bước 6: Kiểm tra các nhánh có thể làm câu trả lời sai

Không cần xây full hypothesis matrix như `investigate-and-plan`.

Tuy nhiên nếu nhiều nhánh có thể tạo cùng triệu chứng, phải xác định chúng.

Ví dụ `401` có thể do:

- Missing token.
- Invalid token.
- Expired token.
- User inactive.
- Internal auth failure.

Không được chọn một nhánh chỉ dựa trên status code.

Phải tìm condition thực tế hoặc ghi:

`Chưa xác định`.

---

### Bước 7: Đối chiếu các thành phần

Nếu câu hỏi liên quan nhiều implementation, phải so sánh theo capability hoặc execution contract.

Ví dụ:

> "Library auth và AiOS có đang làm cùng việc không?"

Phải phân biệt:

- OIDC login.
- OIDC ID Token.
- JWT issuing.
- JWT verification.
- API Access Token.
- Local session.
- Current user.
- Principal.
- Authorization.
- User provisioning.
- S2S authentication.

Hai component cùng sử dụng JWT không có nghĩa chúng duplicate cùng một chức năng.

---

### Bước 8: Trả lời trực tiếp

Mỗi câu hỏi phải được trả lời trực tiếp trước.

Cấu trúc:

**Trả lời:**

[Câu trả lời ngắn gọn.]

**Logic hiện tại:**

`Điểm bắt đầu → xử lý → dependency/service → kết quả`

**Bằng chứng:**

- `[path: symbol, lines]` — giải thích.
- `[path: symbol, lines]` — giải thích.

**Trạng thái kết luận:**

- Đã xác nhận.
- Suy luận.
- Chưa xác định.

---

### Bước 9: Nêu phần chưa xác định

Nếu thiếu evidence, ghi:

- Thiếu gì.
- Vì sao cần.
- Evidence nào có thể xác nhận.

Không hỏi người dùng thông tin có thể tự tìm.

Chỉ hỏi khi:

- Đây là business requirement không có trong source.
- Cần quyết định của người dùng.
- Cần credential/quyền truy cập Agent không có.
- Runtime nằm ngoài phạm vi có thể truy cập.

---

### Bước 10: Dừng đúng phạm vi

Sau khi trả lời:

- Không tự lập Final Plan.
- Không tự đề xuất implementation chi tiết.
- Không tự code.
- Không tự chuyển Skill.
- Không mở rộng thành review toàn hệ thống.

Nếu cần nhiệm vụ tiếp theo, chỉ ghi ngắn:

> Phần này cần một nhiệm vụ `investigate-and-plan` riêng nếu muốn xác định root cause đầy đủ và lập kế hoạch sửa.

Sau đó dừng.

---

## 10. Kiểm tra cấu hình

Khi câu hỏi liên quan config, phải phân biệt:

### Giá trị khai báo

Ví dụ `.env`.

### Giá trị mặc định

Ví dụ default trong Settings class.

### Giá trị process thực tế

Ví dụ environment bên trong Docker container.

### Giá trị được resolve runtime

Ví dụ Config Server hoặc secret manager.

Không được kết luận:

`.env có X → process đang dùng X`

nếu chưa kiểm tra precedence/runtime.

Khi báo config:

- Ghi source.
- Ghi tên field.
- Ghi configured hay không.
- Ghi empty hay không.
- Ghi effective value nếu không nhạy cảm.
- Ghi consumer.

Không in:

- Secret.
- Token.
- Password.
- Private key.
- Credential.

Với secret chỉ báo dạng:

`Configured: YES/NO`

hoặc fingerprint/redacted nếu cần đối chiếu.

---

## 11. Kiểm tra log

Log là runtime evidence nhưng không được diễn giải quá mức.

Ví dụ:

`POST /api/navigation → 503`

chỉ chứng minh endpoint trả 503.

Nó không tự chứng minh:

- Config thiếu.
- Database lỗi.
- Authentication failure.
- Downstream service lỗi.

Phải trace condition tạo status đó.

Nếu nhiều log có cùng:

- correlation ID;
- request ID;
- conversation ID;
- message UUID;

thì có thể nối thành một execution flow.

Không gộp log từ request khác nếu không có evidence.

Nếu event xuất hiện nhiều lần:

- Không tự coi là duplicate bug.
- Kiểm tra lifecycle/retry/streaming semantics.

---

## 12. Kiểm tra Docker/container/runtime

Khi câu hỏi yêu cầu kiểm tra Docker hoặc phụ thuộc container, được phép kiểm tra read-only:

- Container đang chạy.
- Image/tag.
- Command/entrypoint.
- Logs.
- Environment variable presence.
- Network mapping.
- Health state.
- Mounted volume.
- Process.
- Compose rendered configuration.

Không được:

- Restart.
- Recreate.
- Stop.
- Remove.
- Build.

trừ khi người dùng yêu cầu rõ ràng trong nhiệm vụ triển khai phù hợp.

Nếu source được baked vào image:

- Ghi nhận khi liên quan.
- Không mặc định workspace hiện tại giống code container đang chạy.

---

## 13. Kiểm tra database

Nếu cần đọc database:

- Chỉ query read-only.
- Không INSERT.
- Không UPDATE.
- Không DELETE.
- Không ALTER.
- Không migration.
- Không tạo dữ liệu test trên DB thật.

Nếu không kết nối được:

- Ghi rõ runtime DB chưa được kiểm chứng.
- Không suy luận record hiện tại từ schema default.

Ví dụ:

`User.role default=user`

không chứng minh:

`account hiện tại role=user`.

---

## 14. Kiểm tra API

Nếu cần gọi API để xác minh:

- Ưu tiên endpoint/read operation không làm thay đổi dữ liệu.
- Không gọi endpoint có side effect chỉ để thử nếu chưa được phép.
- Có thể dùng source inspection hoặc mocked/test environment khi phù hợp.

Không expose:

- Raw token.
- Cookie value.
- Password.
- Secret.
- Private credential.

---

## 15. Nhiều project hoặc library

Nếu flow đi qua nhiều project:

- Kiểm tra đúng boundary.
- Không coi project A là source of truth cho project B nếu chưa chứng minh.

Ví dụ:

`icomm.python.authentication` trong C04

không tự động chứng minh:

`AiOS phải dùng cùng audience, DB hoặc authorization contract`.

Phải phân biệt:

- Shared/generic capability.
- Project-specific adapter.
- Vendor/copy implementation.
- Runtime consumer thực tế.

Nếu library được vendor/copy:

- Xác định bản runtime đang sử dụng.
- Không mặc định sửa source library gốc sẽ thay đổi bản vendor.

---

## 16. Behavior hiện tại và kiến trúc mong muốn

Skill này chủ yếu trả lời:

> Hệ thống HIỆN TẠI đang làm gì?

Nếu implementation khác documentation hoặc contract:

Có thể nói:

> Implementation hiện tại đang làm X, trong khi documentation/contract mô tả Y.

Không tự kết luận:

> Phải refactor thành Z.

trừ khi người dùng hỏi đánh giá kiến trúc.

Nếu người dùng hỏi kiến trúc:

- Có thể phân tích và so sánh.
- Không tự lập implementation plan nếu chưa được yêu cầu.

---

## 17. Câu hỏi "tại sao"

Không phải câu hỏi có chữ "tại sao" nào cũng cần `investigate-and-plan`.

Ví dụ:

> "Tại sao API này trả 403?"

Nếu trace trực tiếp được:

`route → dependency → condition → 403`

thì `inspect-and-answer` đủ.

Skill này được phép xác định nguyên nhân trực tiếp để trả lời câu hỏi.

Chuyển sang `investigate-and-plan` khi mục tiêu trở thành:

> "Tìm root cause đầy đủ và cho kế hoạch sửa."

---

## 18. Phát hiện ngoài câu hỏi

Nếu phát hiện thêm vấn đề:

### Ảnh hưởng trực tiếp đến câu trả lời

Có thể nêu ngắn gọn.

### Không ảnh hưởng trực tiếp

Không mở rộng phân tích.

Có thể ghi ở mục `Phát hiện liên quan` nếu:

- Có evidence rõ.
- Người dùng cần biết để không hiểu sai.
- Không biến thành nhiệm vụ mới.

Không tạo danh sách dài các cải tiến không liên quan.

---

## 19. Yêu cầu về bằng chứng

Mọi nhận định quan trọng phải có dẫn chiếu.

Định dạng ưu tiên:

`đường/dẫn/tệp: Class/function/symbol, dòng X-Y`

Nếu không có số dòng:

`đường/dẫn/tệp: Class/function/symbol`

Mỗi evidence phải giải thích:

1. Đoạn code/config/log đang làm gì.
2. Vì sao liên quan.
3. Nó hỗ trợ kết luận nào.
4. Là source evidence hay runtime evidence.
5. Chứng minh trực tiếp hay hỗ trợ suy luận.

Không được:

- Chỉ dump danh sách file.
- Chỉ ghi line number.
- Paste code không giải thích.
- Dùng tên function làm evidence khi chưa đọc body.
- Dùng comment làm source of truth khi code thực tế khác.
- Dùng test mock làm runtime evidence.
- Dùng tài liệu cũ thay cho source/runtime mà không đối chiếu.

---

## 20. Nhiều câu hỏi

Nếu người dùng đưa nhiều câu hỏi:

1. Trả lời đúng thứ tự.
2. Không gộp câu hỏi khác nhau thành một kết luận.
3. Mỗi câu có evidence riêng.
4. Có thể dùng lại evidence nếu cùng flow.
5. Nếu câu sau phụ thuộc câu trước, nói rõ.
6. Không bỏ câu hỏi khó và chỉ trả lời câu dễ.
7. Câu nào thiếu evidence phải ghi `Chưa xác định` riêng.

---

## 21. Không hỏi điều có thể tự kiểm tra

Không hỏi:

- File ở đâu?
- Function nằm ở file nào?
- Container tên gì?
- Frontend gọi endpoint nào?
- Config default là gì?
- Có test không?

nếu codebase hoặc runtime tools có thể tự xác định.

Chỉ hỏi khi:

- Cần business requirement không có trong source.
- Cần người dùng quyết định giữa nhiều behavior hợp lệ.
- Cần credential/quyền Agent không có.
- Cần xác nhận ý định của người dùng.
- Runtime ngoài phạm vi Agent có thể truy cập.

---

## 22. Không tự biến câu hỏi thành sửa lỗi

Ví dụ người dùng hỏi:

> "Tại sao user thường không load được Apps?"

Nếu xác nhận:

`/apps/options → require_iam_admin → user.role != admin → 403`

thì trả lời đúng điều đó.

Không tự:

- đổi dependency;
- viết permission matrix toàn hệ thống;
- sửa code;
- lập Final Plan.

Nếu người dùng tiếp tục:

> "Tìm root cause và cho plan sửa."

thì chuyển sang nhiệm vụ `investigate-and-plan`.

---

## 23. Định dạng kết quả bắt buộc

### 1. Phạm vi đã kiểm tra

Nêu ngắn:

- Project/module.
- Tệp chính.
- Runtime/log/config đã kiểm tra.
- Luồng đã trace.
- Phạm vi chưa kiểm tra được.

Không cần liệt kê mọi file đã search.

### 2. Trả lời từng câu hỏi

Với mỗi câu:

#### Câu hỏi N: [Nội dung]

**Trả lời:**

[Câu trả lời trực tiếp.]

**Logic hiện tại:**

`Điểm bắt đầu → xử lý → dependency/service → kết quả`

**Bằng chứng:**

- `[path: symbol, lines]` — giải thích.
- `[path: symbol, lines]` — giải thích.

**Trạng thái kết luận:**

- Đã xác nhận.
- Suy luận.
- Chưa xác định.

**Nội dung chưa xác định:**

Chỉ ghi khi thực sự còn thiếu evidence.

### 3. Kết luận chung

Chỉ thêm nếu các câu hỏi liên hệ trực tiếp.

Nêu ngắn:

- Flow tổng thể.
- Quan hệ giữa câu trả lời.
- Điểm quan trọng nhất.

Không biến thành Final Plan.

### 4. Phát hiện liên quan

Chỉ thêm khi:

- Có evidence rõ.
- Ảnh hưởng trực tiếp đến cách hiểu.
- Người dùng cần biết.

Không đề xuất implementation chi tiết.

### 5. Trạng thái kiểm chứng

Chỉ thêm bảng khi nhiệm vụ phụ thuộc runtime:

| Hạng mục | Trạng thái |
|---|---|
| Source behavior | Đã kiểm tra / Chưa kiểm tra |
| Runtime config | Đã kiểm tra / Chưa kiểm tra |
| Runtime request | Đã kiểm tra / Chưa kiểm tra |
| Database state | Đã kiểm tra / Chưa kiểm tra |

---

## 24. Điểm dừng

Sau khi trả lời đầy đủ:

- Dừng lại.
- Không chỉnh sửa mã nguồn.
- Không chỉnh sửa config.
- Không tạo patch.
- Không tạo diff.
- Không tạo commit.
- Không lập Final Plan.
- Không tự triển khai.
- Không tự chuyển sang Skill khác.

Nếu cần điều tra root cause hoặc sửa code:

Chỉ ghi:

> Vấn đề này cần một nhiệm vụ `investigate-and-plan` riêng nếu muốn tiếp tục xác định root cause đầy đủ và lập kế hoạch sửa.

Sau đó dừng.

---

## 25. Checklist hoàn thành

Trước khi trả kết quả, tự kiểm tra:

- Đã hiểu đúng câu hỏi người dùng.
- Đã đọc rules áp dụng.
- Đã đọc source thực tế.
- Đã trace đủ luồng.
- Không trace lan rộng không cần thiết.
- Đã kiểm tra runtime nếu câu hỏi phụ thuộc runtime và môi trường cho phép.
- Không coi default config là runtime value.
- Không coi HTTP status tự nó là root cause.
- Không coi test mock là runtime evidence.
- Đã phân biệt `Đã xác nhận / Suy luận / Chưa xác định`.
- Mỗi kết luận quan trọng có evidence.
- Không hỏi người dùng điều có thể tự xác định.
- Không tự chuyển thành root-cause investigation.
- Không lập plan khi người dùng chỉ hỏi.
- Không chỉnh sửa mã nguồn hoặc trạng thái hệ thống.
- Đã trả lời trực tiếp trước khi giải thích dài.
- Đã dừng đúng phạm vi.