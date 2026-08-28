# Bài 12 — OOP cơ bản (class, object) · Lý thuyết

> Track: Cơ bản (Beginner) · Module 1 · Bài 12

## 📖 1. Kiến thức cơ bản

### 1.1. OOP là gì? Vì sao cần?
Cho đến giờ bạn dùng biến rời rạc để mô tả sự vật. Ví dụ một chú chó: `ten_cho = "Milu"`, `tuoi_cho = 3`. Nếu có 100 con chó thì quản lý rất rối.

OOP cho phép **gói dữ liệu (thuộc tính) và hành động (method) liên quan vào chung một "hộp"** gọi là object. Hãy tưởng tượng:
- **Class** = bản thiết kế/khuôn bánh (định nghĩa "chó" gồm những gì).
- **Object** = chiếc bánh cụ thể làm ra từ khuôn (con chó Milu, con chó Vàng...).

### 1.2. Tạo class đầu tiên

```python
class ChoCon:
    # __init__ là "hàm khởi tạo" — tự chạy khi tạo object mới
    def __init__(self, ten, tuoi):
        self.ten = ten     # gán tham số vào thuộc tính của object
        self.tuoi = tuoi

# Tạo object (instance) từ class
milu = ChoCon("Milu", 3)   # __init__ được gọi tự động
vang = ChoCon("Vang", 5)

print(milu.ten)    # Milu  → truy cập thuộc tính bằng dấu chấm
print(vang.tuoi)   # 5
```

### 1.3. `self` là gì?
`self` đại diện cho **chính object đang gọi**. Khi viết `milu.ten`, bên trong class `self` chính là `milu`. Nhờ `self`, mỗi object giữ dữ liệu riêng của mình. Bạn **luôn** để `self` là tham số đầu tiên của method, nhưng **không** truyền nó khi gọi (Python tự truyền).

### 1.4. Method — hành động của object
Method là hàm định nghĩa bên trong class, mô tả những gì object có thể làm.

```python
class ChoCon:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def sua(self):                     # method: hành động "sủa"
        print(f"{self.ten} noi: Gau gau!")

    def gioi_thieu(self):
        print(f"Toi la {self.ten}, {self.tuoi} tuoi.")

milu = ChoCon("Milu", 3)
milu.sua()          # Milu noi: Gau gau!   → không cần truyền self
milu.gioi_thieu()   # Toi la Milu, 3 tuoi.
```

Method cũng có thể thay đổi thuộc tính của object:

```python
class TaiKhoan:
    def __init__(self, chu_tk, so_du=0):
        self.chu_tk = chu_tk
        self.so_du = so_du            # số dư ban đầu, mặc định 0

    def nap_tien(self, so_tien):
        self.so_du += so_tien         # cập nhật thuộc tính so_du
        print(f"Da nap {so_tien}. So du moi: {self.so_du}")

tk = TaiKhoan("An")
tk.nap_tien(50000)   # Da nap 50000. So du moi: 50000
tk.nap_tien(20000)   # Da nap 20000. So du moi: 70000
```

### 1.5. Giới thiệu ngắn về kế thừa (inheritance)
Kế thừa cho phép một class **dùng lại** thuộc tính và method của class khác, rồi bổ sung/điều chỉnh. Class con kế thừa từ class cha.

```python
class DongVat:
    def __init__(self, ten):
        self.ten = ten

    def an(self):
        print(f"{self.ten} dang an.")

# Cho kế thừa từ DongVat → tự có sẵn __init__ và method an()
class Cho(DongVat):
    def sua(self):
        print(f"{self.ten} sua: Gau gau!")

milu = Cho("Milu")
milu.an()    # Milu dang an.   → method kế thừa từ DongVat
milu.sua()   # Milu sua: Gau gau!  → method riêng của Cho
```

---

⬅️ Quay lại [Mục lục bài](README.md) · ➡️ Tiếp theo: [Ví dụ minh họa tổng hợp](2-vi-du-tong-hop.md)
