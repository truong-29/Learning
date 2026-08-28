# Bài 04 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 04

## 💡 Ví dụ minh họa tổng hợp

```python
# xep_loai.py — xếp loại học lực theo điểm nhập vào

# Nhận điểm từ người dùng, ép sang float
diem = float(input("Nhập điểm của bạn (0-10): "))

# Kiểm tra điểm hợp lệ trước
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ!")     # điểm ngoài khoảng 0-10
elif diem >= 8:
    print("Học lực: Giỏi")
elif diem >= 6.5:
    print("Học lực: Khá")
elif diem >= 5:
    print("Học lực: Trung bình")
else:
    print("Học lực: Yếu")

print("Đã xếp loại xong.")
```

Nếu nhập `7`, output:

```
Nhập điểm của bạn (0-10): 7
Học lực: Khá
Đã xếp loại xong.
```

Giải thích: chương trình kiểm tra điểm hợp lệ trước, sau đó lần lượt xét từ cao xuống thấp. Với `7`, nhánh `diem >= 6.5` đúng đầu tiên nên in "Khá" rồi dừng chuỗi điều kiện.
