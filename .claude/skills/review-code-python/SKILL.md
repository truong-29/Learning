---
name: review-code-python
description: Review chất lượng code Python sau khi logic chính đã chạy đúng: readability, naming, duplication, responsibility, coupling, testability, error handling và hiệu năng phù hợp trình độ. Không refactor hộ toàn bộ.
---

# Review chất lượng code Python

## 1. Khi dùng

Dùng khi code đã cơ bản chạy đúng hoặc sau khi bài/project qua correctness check.

Nếu code còn sai chức năng chính, ưu tiên `cham-bai-python` hoặc `debug-python` trước.

## 2. Phạm vi review

Chọn tiêu chí phù hợp trình độ:

- naming;
- readability;
- duplication;
- độ dài/trách nhiệm của hàm;
- chia module;
- coupling/cohesion;
- error handling;
- type hints;
- testability;
- complexity;
- performance khi thực sự liên quan.

Không áp tiêu chuẩn production nâng cao cho bài nhập môn.

## 3. Cách phản hồi

Với mỗi finding:

1. Mức: `IMPORTANT` / `SHOULD_IMPROVE` / `OPTIONAL`.
2. Vị trí.
3. Vì sao ảnh hưởng chất lượng code.
4. Câu hỏi/gợi ý để học viên tự refactor.
5. Tiêu chí để biết refactor đã tốt hơn.

Không viết lại toàn bộ module cho học viên.

## 4. Ưu tiên

Mỗi lượt chỉ nên chọn 1–3 vấn đề giá trị nhất.

Không biến review thành danh sách 20 lỗi phong cách khiến học viên mất trọng tâm.

## 5. Sau refactor

Kiểm tra:

- hành vi cũ còn đúng;
- code dễ hiểu hơn thật;
- không thêm abstraction thừa;
- học viên giải thích được lý do thay đổi.
