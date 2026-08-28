# Bài 06 — Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 06

## 💡 Ví dụ minh họa tổng hợp

Chương trình tính điểm trung bình và xếp loại, chia thành các hàm nhỏ:

```python
def tinh_trung_binh(toan, van, anh):
    """Nhận 3 điểm, trả về điểm trung bình."""
    return (toan + van + anh) / 3

def xep_loai(diem_tb):
    """Nhận điểm trung bình, trả về xếp loại."""
    if diem_tb >= 8:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# Chương trình chính dùng lại các hàm trên
tb = tinh_trung_binh(9, 7, 8)
print(f"Điểm trung bình: {tb:.2f}")   # làm tròn 2 chữ số thập phân
print(f"Xếp loại: {xep_loai(tb)}")
```

Giải thích:
- Mỗi hàm làm **một việc rõ ràng**: tính trung bình, và xếp loại.
- Kết quả của `tinh_trung_binh` được truyền tiếp vào `xep_loai` — đây là sức mạnh của `return`.
- Dòng chữ trong `"""..."""` gọi là docstring, dùng để mô tả hàm làm gì.
