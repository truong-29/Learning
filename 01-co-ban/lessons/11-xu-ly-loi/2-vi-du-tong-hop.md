# Bài 11 — Xử lý lỗi (try/except) · Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 11

## 💡 Ví dụ minh họa tổng hợp
Chương trình nhập số an toàn: lặp lại cho đến khi người dùng nhập đúng một số dương, xử lý mọi trường hợp gõ sai mà không bị sập.

```python
def nhap_so_duong(thong_bao):
    while True:                      # lặp mãi cho đến khi nhập đúng
        try:
            gia_tri = int(input(thong_bao))
            if gia_tri <= 0:
                raise ValueError("So phai lon hon 0")  # tự ném lỗi theo quy tắc
        except ValueError as e:
            print(f"Nhap lai! ({e})")   # bắt cả lỗi ép kiểu lẫn lỗi tự ném
        else:
            return gia_tri              # không lỗi → trả về và thoát vòng lặp

tuoi = nhap_so_duong("Nhap tuoi cua ban: ")
print(f"Cam on! Tuoi cua ban la {tuoi}")
```

---

⬅️ Quay lại [Lý thuyết](1-ly-thuyet.md) · ➡️ Tiếp theo: [Lỗi thường gặp](3-loi-thuong-gap.md)
