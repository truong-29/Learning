# Bài 01 — Kiến thức cơ bản

> Track: Cơ bản (Beginner) · Module 1 · Bài 01

## 📖 1. Kiến thức cơ bản

### 1.1. Python là gì? Vì sao học Python?

Hãy tưởng tượng máy tính là một người giúp việc rất chăm chỉ nhưng chỉ hiểu đúng những gì bạn ra lệnh. **Ngôn ngữ lập trình** là cách chúng ta "nói chuyện" với máy tính để ra lệnh. **Python** là một trong những ngôn ngữ dễ học nhất — câu lệnh gần giống tiếng Anh thông thường, rất phù hợp cho người mới bắt đầu.

Python được dùng để làm web, phân tích dữ liệu, trí tuệ nhân tạo, tự động hóa công việc... nên học Python mở ra rất nhiều cơ hội việc làm.

### 1.2. Cài đặt Python

1. Mở trình duyệt, vào trang chính thức: **https://www.python.org/downloads/**
2. Bấm nút vàng lớn để tải phiên bản mới nhất (ví dụ Python 3.12).
3. Mở file vừa tải về để cài đặt.
4. **QUAN TRỌNG (Windows):** ở màn hình đầu tiên, hãy tick vào ô **"Add Python to PATH"** rồi mới bấm *Install Now*. Bước này giúp máy tính "tìm thấy" Python từ bất cứ đâu.

Sau khi cài xong, ta cần kiểm tra xem Python đã sẵn sàng chưa. Mở **Terminal** (trên Windows là *Command Prompt* hoặc *PowerShell*; trên Mac là *Terminal*) và gõ:

```bash
python --version
```

Nếu máy hiện ra dòng như `Python 3.12.1` nghĩa là bạn đã cài thành công. (Trên một số máy Mac/Linux bạn cần gõ `python3 --version`.)

### 1.3. Cài đặt VS Code — nơi để viết code

Bạn có thể viết code bằng Notepad, nhưng lập trình viên dùng công cụ chuyên dụng gọi là **trình soạn thảo code**. Phổ biến và miễn phí nhất là **VS Code (Visual Studio Code)**.

1. Vào **https://code.visualstudio.com/** và tải về, cài đặt bình thường.
2. Mở VS Code, bấm vào biểu tượng **Extensions** (hình 4 ô vuông) ở thanh bên trái.
3. Gõ tìm **"Python"** (của Microsoft) và bấm **Install**. Tiện ích này giúp VS Code hiểu và hỗ trợ bạn viết Python tốt hơn.

### 1.4. Chương trình đầu tiên — hàm `print()`

`print()` là một **hàm** có sẵn của Python. Hãy hiểu nó đơn giản là câu lệnh: "In ra màn hình những gì tôi đưa cho bạn". Nội dung cần in được đặt trong dấu ngoặc đơn `()`, và nếu là chữ thì phải bọc trong dấu nháy `"..."`.

```python
# Dòng chữ sau dấu # là "comment" (chú thích), máy tính bỏ qua, chỉ để con người đọc
print("Xin chào, thế giới!")  # In ra dòng chữ Xin chào, thế giới!
```

Kết quả in ra màn hình (gọi là **output**):

```
Xin chào, thế giới!
```

Bạn có thể `print` nhiều dòng, mỗi lệnh `print` sẽ xuống một dòng mới:

```python
print("Tôi đang học Python.")   # Dòng 1
print("Thật là thú vị!")        # Dòng 2
```

Output:

```
Tôi đang học Python.
Thật là thú vị!
```

### 1.5. Cách chạy một file `.py`

Code Python được lưu trong file có đuôi `.py`. Các bước:

1. Trong VS Code, chọn **File → Open Folder** và mở thư mục `code/` của bạn (ví dụ `code/25-08-2026/`).
2. Tạo file mới tên `hello.py` (chuột phải → New File, gõ tên kèm đuôi `.py`).
3. Gõ nội dung sau vào file:

```python
print("Chương trình đầu tiên của tôi!")
```

4. Lưu file lại (`Ctrl + S`).
5. Mở terminal ngay trong VS Code bằng menu **Terminal → New Terminal**, rồi gõ:

```bash
python hello.py
```

Máy tính sẽ đọc file và in ra:

```
Chương trình đầu tiên của tôi!
```

> Mẹo: bạn cũng có thể bấm nút ▶ (Run) ở góc trên bên phải VS Code để chạy nhanh.
