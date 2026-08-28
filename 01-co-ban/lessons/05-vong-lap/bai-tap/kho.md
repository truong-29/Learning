# Bài 05 — Bài tập

> Track: Cơ bản (Beginner) · Module 1 · Bài 05
> Độ khó: Khó (Hard)

Các bài này gần với bài toán thực tế và cần kết hợp `for`, `while`, `break`, `continue`, vòng lặp lồng nhau cùng xử lý trường hợp biên. Nếu bí, xem [gợi ý hướng dẫn](../goi-y/huong-dan.md) (không phải lời giải sẵn).

1. **Máy tính bỏ túi mini**: Lặp liên tục hỏi người dùng nhập một phép tính đơn giản dạng `a + b` (hoặc `-`, `*`, `/`). Sau mỗi lần tính, in kết quả rồi hỏi tiếp. Khi người dùng gõ `thoat` thì dừng chương trình. Phải xử lý trường hợp chia cho 0 (không cho chương trình sập, in thông báo lỗi và tiếp tục).

2. **In tất cả số nguyên tố nhỏ hơn N**: Nhập `N`, in ra mọi số nguyên tố trong khoảng từ 2 đến N. Với mỗi số phải dùng một vòng lặp kiểm tra nguyên tố (vòng lặp lồng nhau). Cố gắng chỉ cần kiểm tra ước tới căn bậc hai của số đó để chạy nhanh hơn.

3. **Vẽ hình kim tự tháp cân giữa**: Nhập chiều cao `n`, in ra kim tự tháp dấu sao căn giữa. Ví dụ với `n = 4`:

   ```
      *
     ***
    *****
   *******
   ```

   Mỗi dòng gồm phần khoảng trắng bên trái rồi tới dấu sao; số sao là số lẻ tăng dần (1, 3, 5, 7...).
