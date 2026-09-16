---
name: sinh-lo-trinh-python
description: Nghiên cứu rồi sinh động curriculum Python Trung cấp, Nâng cao, mini-project, project lớn và capstone dựa trên năng lực thực tế của học viên. Chỉ dùng khi orchestrator xác nhận đủ điều kiện hoặc cần bridge curriculum.
---

# Sinh lộ trình và nội dung Python động

## 1. Mục đích

Skill này tạo NỘI DUNG HỌC MỚI khi học viên đã đủ nền hoặc khi cần một bridge nhỏ.

Không dùng skill này để dạy trực tiếp một bài đang có.
Không dùng skill này để chấm bài.

## 2. Điều kiện kích hoạt

Chỉ sinh curriculum khi có một trong các điều kiện:

- `learning-orchestrator-python` kết luận `TRACK_READY`.
- `learning-orchestrator-python` kết luận `BRIDGE_REQUIRED` và cần một cụm bài ngắn để lấp lỗ hổng.
- Học viên chủ động yêu cầu tạo một chuyên đề/project mới phù hợp trình độ hiện tại.

Nếu chưa có bằng chứng readiness, quay lại orchestrator thay vì tự nâng độ khó.

## 3. Phải nghiên cứu trước khi sinh

Trước khi chốt một curriculum mới:

1. Đọc toàn bộ nội dung track trước đã học.
2. Đọc `PROGRESS.md`, sổ điểm, lỗi lặp lại và các project/bài tổng hợp gần nhất.
3. Xác định năng lực đã có và năng lực còn thiếu.
4. Nếu môi trường có web/search:
   - nghiên cứu tài liệu Python chính thức và nguồn kỹ thuật đáng tin cậy;
   - ưu tiên kiến thức hiện đại, còn phù hợp với Python hiện hành;
   - dùng nghiên cứu để xác nhận thứ tự, phạm vi và tính thực tế của chủ đề;
   - không copy nguyên văn nguồn.
5. Nếu không có web/search: được dùng kiến thức mô hình, nhưng phải ghi rõ curriculum được sinh từ kiến thức nội tại, chưa được đối chiếu nguồn ngoài.

Không được giả vờ đã nghiên cứu web khi chưa làm.

## 4. Nguyên tắc sinh curriculum

Curriculum phải:

- nối trực tiếp từ kiến thức học viên đã có;
- tránh lặp vô ích bài đã học;
- ưu tiên kỹ năng dùng thật thay vì kiến thức hiếm chỉ để "nâng cao";
- tăng dần tỷ trọng tự code, debug, test, refactor và project;
- mỗi bài có đầu ra năng lực rõ ràng;
- chỉ đưa kiến thức cần thiết cho chặng hiện tại.

Không sinh toàn bộ tương lai nếu chưa cần.

Mặc định sinh theo **chặng 4–6 bài** hoặc một module logic tương đương. Sau khi học xong chặng, orchestrator đánh giá lại rồi mới sinh chặng tiếp theo.

## 5. Định hướng theo track

### `02-trung-cap`

Ưu tiên các nhóm năng lực như:

- chia nhỏ chương trình bằng hàm/module/package;
- collections/comprehension phù hợp;
- file, JSON/CSV;
- exception và error handling;
- OOP và composition ở mức thực dụng;
- type hint;
- iterator/generator khi phù hợp;
- môi trường, dependency;
- debugging;
- clean code/refactor cơ bản;
- test cơ bản nếu nền đã đủ.

Không bắt buộc nhồi tất cả cùng lúc; chọn theo prerequisite thực tế.

### `03-nang-cao`

Ưu tiên:

- Python data model và mutability/identity khi có ích;
- typing nâng cao vừa đủ;
- testing sâu hơn, fixture/mock;
- architecture, separation of concerns;
- SOLID/pattern ở mức ứng dụng, không học thuộc;
- database/ORM;
- HTTP/API;
- async/concurrency;
- profiling/performance;
- logging/config/security cơ bản;
- packaging/deployment phù hợp;
- Git workflow nếu cần cho project.

### `04-du-an`

Không phải track lý thuyết tuyến tính.
Sinh dự án theo năng lực đã có, gồm:

- mini-project;
- intermediate project;
- advanced project;
- capstone.

## 6. Cấu trúc mỗi bài được sinh

Mỗi lesson nên có tối thiểu:

```text
<track>/lessons/NN-ten-bai/
├── README.md
├── 1-ly-thuyet.md
├── 2-vi-du-tong-hop.md
├── 3-loi-thuong-gap.md
├── 4-debug-lab.md
└── bai-tap/
    ├── de.md
    ├── trung-binh.md
    └── kho.md
```

Có thể thêm `challenge/` hoặc `project-task/` nếu bài phù hợp.

## 7. Yêu cầu nội dung lesson

### `README.md`

Phải có:

- prerequisite;
- mục tiêu đầu ra;
- vì sao bài này xuất hiện lúc này;
- tiêu chí completion;
- liên hệ với bài trước/bài sau.

### Lý thuyết

- ngắn, tập trung;
- có ví dụ nhỏ;
- không biến thành tài liệu tham khảo khổng lồ.

### Bài tập

- Dễ: kiểm tra một khái niệm chính.
- Trung bình: phối hợp 2–3 khái niệm.
- Khó: bài tổng hợp vừa sức, yêu cầu suy nghĩ nhưng không dùng kiến thức chưa học.

### Debug lab

Phải có ít nhất một lỗi thực tế phù hợp bài, yêu cầu học viên tìm nguyên nhân thay vì chỉ viết code mới.

## 8. Sinh project

Project phải được tạo từ các năng lực học viên đã có.

Mỗi project gồm:

```text
04-du-an/<project-name>/
├── README.md
├── REQUIREMENTS.md
├── MILESTONES.md
├── ACCEPTANCE.md
└── REVIEW.md
```

`REQUIREMENTS.md` mô tả yêu cầu sản phẩm, KHÔNG biến thành lời giải kỹ thuật chi tiết.

`MILESTONES.md` chia chặng, nhưng không viết code hay quyết định hộ toàn bộ kiến trúc.

`ACCEPTANCE.md` chứa tiêu chí chạy đúng, test, chất lượng code và hành vi biên phù hợp.

## 9. Sinh bài tập lớn / capstone

Chỉ sinh capstone khi học viên đã có bằng chứng:

- tự phân tích yêu cầu;
- chia chương trình thành module/component hợp lý;
- tự debug được lỗi phổ biến;
- biết viết hoặc hiểu test ở mức phù hợp;
- biết refactor sau khi code chạy;
- đã hoàn thành ít nhất một project nhỏ hơn với mức hỗ trợ không quá cao.

Capstone phải có requirement gần thực tế và không cho sẵn từng bước cài đặt.

## 10. Lưu và đóng băng curriculum đã sinh

Mỗi curriculum/chặng sau khi được chốt phải được lưu thành file thật trong `Learning/`; từ thời điểm đó nó trở thành source of truth cho `day-bai-python` và `cham-bai-python`.

Duy trì registry `Learning/CURRICULUM.md` với tối thiểu:

- track/chặng hiện tại;
- trạng thái `planned` / `active` / `completed`;
- lý do chặng này được sinh;
- prerequisite đã dùng để quyết định;
- danh sách lesson/project đã tạo;
- nguồn nghiên cứu chính nếu có;
- ngày/phiên sinh nếu hệ thống có timestamp.

Không âm thầm viết lại lesson/curriculum đã active chỉ vì lần chạy sau mô hình nghĩ ra thứ tự khác. Nếu cần thay đổi:

1. nêu lý do;
2. kiểm tra ảnh hưởng tới progress hiện tại;
3. cập nhật registry;
4. giữ nguyên nội dung đã học trừ khi thật sự sai hoặc học viên yêu cầu sửa.

## 11. Chống over-generation

Sau mỗi lần sinh:

- chỉ tạo nội dung cần cho chặng tiếp theo;
- ghi rõ vì sao các bài này được chọn;
- ghi prerequisite và mục tiêu;
- để orchestrator đánh giá lại sau khi chặng hoàn thành.

Không sinh "100 bài Python hoàn chỉnh" trong một lần trừ khi học viên yêu cầu rõ.
