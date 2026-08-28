# Lộ trình học Python → Lập trình viên

Chào mừng bạn đến với hành trình học Python từ con số 0 để trở thành lập trình viên!

## 📁 Kiến thức được lưu ở đâu?

Tất cả nằm trong thư mục này (`Learning/`), dưới dạng file Markdown (`.md`) — mở bằng VS Code hoặc trình duyệt là đọc được, không cần internet.

## 🎚️ Cấu trúc theo 2 thang chuẩn

Khóa học tổ chức theo **2 thang đo chuẩn** trong ngành (để bạn tra cứu ở đâu cũng khớp):

**1. Cấp độ TRACK — theo trình độ người học** (chuẩn Beginner → Intermediate → Advanced):

| Thư mục | Tên | Chuẩn quốc tế | Mục tiêu |
|---------|-----|---------------|----------|
| `01-co-ban/`   | Cơ bản   | Beginner     | Hiểu cú pháp, viết chương trình nhỏ |
| `02-trung-cap/`| Trung cấp| Intermediate | Viết code Pythonic, tổ chức dự án, dùng thư viện, viết test |
| `03-nang-cao/` | Nâng cao | Advanced     | Giải thuật, hiệu năng, kiến trúc, giải bài khó |

**2. Độ khó BÀI TẬP — trong mỗi bài học** (chuẩn LeetCode Easy/Medium/Hard):

| File | Tên | Chuẩn | Ý nghĩa |
|------|-----|-------|---------|
| `bai-tap/de.md`         | Dễ         | Easy   | Áp dụng trực tiếp 1 khái niệm vừa học |
| `bai-tap/trung-binh.md` | Trung bình | Medium | Kết hợp nhiều khái niệm, nhiều bước |
| `bai-tap/kho.md`        | Khó        | Hard   | Bài toán mở, tối ưu, xử lý biên, gần thực tế/phỏng vấn |

## 🗂️ Cấu trúc thư mục

```
Learning/
├── README.md                 ← File này (giới thiệu + chuẩn cấp độ)
├── PROGRESS.md               ← BẢN ĐỒ HỌC + đánh dấu tiến độ (mở mỗi ngày)
├── 01-co-ban/                ← TRACK Cơ bản (Beginner)
│   ├── README.md             ← giới thiệu track + danh sách bài
│   └── lessons/NN-ten-bai/
│       ├── README.md         ← mục lục bài (mục tiêu + link)
│       ├── 1-ly-thuyet.md    ← lý thuyết + ví dụ giải thích
│       ├── 2-vi-du-tong-hop.md
│       ├── 3-loi-thuong-gap.md
│       ├── bai-tap/          ← de.md · trung-binh.md · kho.md
│       └── goi-y/huong-dan.md ← HƯỚNG DẪN gợi mở (không có đáp án đầy đủ)
├── 02-trung-cap/README.md    ← TRACK Trung cấp (lộ trình bài học)
├── 03-nang-cao/README.md     ← TRACK Nâng cao (lộ trình bài học)
└── code/                     ← nơi BẠN viết code thực hành (theo ngày)
```

## 💡 Vì sao phần gợi ý KHÔNG cho đáp án đầy đủ?

File `goi-y/huong-dan.md` cố tình KHÔNG đưa lời giải hoàn chỉnh. Thay vào đó nó hướng dẫn: nên dùng hàm/khái niệm nào, hàm đó hoạt động ra sao, các bước logic và cách liên kết — để **bạn tự viết code**. Tự viết mới thực sự học được; đọc lời giải sẵn thì không.

## 🗺️ Cách sử dụng

1. Mở `PROGRESS.md` — bản đồ tổng thể, xem bài tiếp theo.
2. Vào bài học: đọc `1-ly-thuyet.md` → `2-vi-du-tong-hop.md` → `3-loi-thuong-gap.md`.
3. Làm bài tập theo thứ tự `de` → `trung-binh` → `kho`. Bí thì mở `goi-y/huong-dan.md` (chỉ gợi ý, không phải đáp án).
4. Viết code thực hành trong `code/<ngày>/`. Luôn gõ tay.
5. Đánh dấu `[x]` trong `PROGRESS.md` khi xong.

## 🎯 Nguyên tắc học

- Code mỗi ngày, đều đặn hơn là dồn.
- 80% thực hành, 20% lý thuyết.
- Gõ tay, không copy-paste.
- Sai và debug là học.

## 💬 Trợ lý học tập

Bạn có thể nhờ trợ lý (Claude): giải thích khái niệm, chấm/sửa code, ra thêm bài tập, đánh dấu tiến độ, hoặc soạn chi tiết các bài track Trung cấp/Nâng cao khi bạn tới đó.

## 🧑‍🏫 2 Skill hỗ trợ học (đặt trong `.claude/skills/`)

Trợ lý có sẵn 2 skill chuyên cho việc học. Bạn không cần gọi tên skill — chỉ cần nói theo mẫu dưới, trợ lý sẽ tự áp dụng.

**1. `day-bai-python` — Giáo viên dẫn học từng bài**
Dùng khi muốn được dạy kiến thức MỚI, từng bước, có kiểm tra hiểu bài.
- Ví dụ nói: *"Dạy mình Bài 05"* hoặc *"Hướng dẫn mình học bài vòng lặp"*.
- Trợ lý sẽ: giảng từng khái niệm nhỏ → dừng hỏi bạn đã hiểu chưa → cho đoán kết quả / micro-bài tập → mới đi tiếp. Khi dạy có thể đưa code ví dụ minh họa.

**2. `cham-bai-python` — Chấm bài & hướng dẫn sửa**
Dùng khi bạn đã TỰ VIẾT code bài tập và muốn được chấm.
- Ví dụ nói: *"Chấm giúp mình bài Dễ số 3 của Bài 05"* rồi dán code (hoặc chỉ file trong `code/<ngày>/`).
- Trợ lý sẽ: cho điểm (thang 10) → khen chỗ đúng → chỉ chỗ sai + vì sao → hướng dẫn cách tự sửa.

> Nguyên tắc chung của cả 2 skill: KHÔNG đưa code lời giải bài tập. Chỉ hướng dẫn bằng lời và gợi mở để BẠN tự viết — vì tự viết mới thực sự học được.

Chúc bạn học tốt! 🚀
