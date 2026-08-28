# Bài 12 — OOP cơ bản (class, object) · Ví dụ minh họa tổng hợp

> Track: Cơ bản (Beginner) · Module 1 · Bài 12

## 💡 Ví dụ minh họa tổng hợp
Class `HocSinh` quản lý tên và danh sách điểm, có method thêm điểm và tính điểm trung bình:

```python
class HocSinh:
    def __init__(self, ten):
        self.ten = ten
        self.diem = []               # danh sách điểm, ban đầu rỗng

    def them_diem(self, d):
        self.diem.append(d)          # thêm 1 điểm vào danh sách

    def diem_trung_binh(self):
        if not self.diem:            # nếu chưa có điểm nào
            return 0
        return sum(self.diem) / len(self.diem)

    def xep_loai(self):
        tb = self.diem_trung_binh()
        if tb >= 8:
            return "Gioi"
        elif tb >= 6.5:
            return "Kha"
        else:
            return "Trung binh"

# Sử dụng
hs = HocSinh("An")
hs.them_diem(9)
hs.them_diem(8)
hs.them_diem(7)
print(f"Hoc sinh: {hs.ten}")
print(f"Diem TB: {hs.diem_trung_binh():.2f}")   # 8.00
print(f"Xep loai: {hs.xep_loai()}")             # Gioi
```

---

⬅️ Quay lại [Lý thuyết](1-ly-thuyet.md) · ➡️ Tiếp theo: [Lỗi thường gặp](3-loi-thuong-gap.md)
