---
name: luyen-tap-python
description: Tạo bài luyện Python thích nghi theo kiến thức đã học, điểm số và lỗi lặp lại. Không dạy kiến thức mới và không đưa lời giải hoàn chỉnh.
---

# Luyện tập Python thích nghi

## 1. Mục tiêu

Tạo bài tập để củng cố đúng phần học viên cần luyện, thay vì phát bài ngẫu nhiên.

## 2. Dữ liệu đầu vào

Đọc:

- `PROGRESS.md`;
- bài học đã hoàn thành;
- sổ điểm;
- lỗi gần đây;
- code gần nhất nếu có.

Chỉ dùng kiến thức học viên đã học, trừ khi bài được đánh dấu rõ là preview/tự chọn.

## 3. Chọn mục tiêu luyện

Ưu tiên theo thứ tự:

1. Khái niệm đang sai lặp lại.
2. Khái niệm hiểu lý thuyết nhưng chưa dùng độc lập được.
3. Kiến thức cũ lâu chưa dùng.
4. Bài phối hợp nhiều kiến thức đã học.

## 4. Sinh bài

Mỗi phiên mặc định chỉ sinh 1–3 bài.

Mỗi bài phải ghi:

- mục tiêu kỹ năng;
- kiến thức được phép dùng;
- yêu cầu;
- input/output hoặc tiêu chí kiểm tra nếu cần;
- độ khó tương đối.

Không ghi lời giải.

## 5. Adaptive difficulty

- Làm đúng nhanh, ít hint → tăng độ tổng hợp.
- Làm đúng nhưng cần nhiều hint → giữ độ khó, đổi ngữ cảnh.
- Sai do kiến thức nền → giảm phạm vi và gọi `day-bai-python`/`on-tap-python` nếu cần.
- Sai do debugging → chuyển `debug-python`.

## 6. Readiness-check

Khi được orchestrator yêu cầu, có thể tạo readiness-check gồm 2–4 nhiệm vụ ngắn bao phủ các năng lực cốt lõi đã học.

Readiness-check không được đưa kiến thức mới và không được tối ưu để "đánh đố".
