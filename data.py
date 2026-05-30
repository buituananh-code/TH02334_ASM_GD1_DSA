import pandas as pd

# Khởi tạo danh sách dữ liệu các đơn hàng
orders = [
    {"order_id": "PS008", "customer": "An", "area": "Ha Noi", "weight": 4.5, "fee": 45000, "created_at": "2026-05-01 09:15"},
    {"order_id": "PS003", "customer": "Binh", "area": "Da Nang", "weight": 2.0, "fee": 30000, "created_at": "2026-05-01 08:20"},
    {"order_id": "PS001", "customer": "Chi", "area": "Ho Chi Minh", "weight": 6.2, "fee": 60000, "created_at": "2026-05-01 10:05"},
    {"order_id": "PS010", "customer": "Dung", "area": "Ha Noi", "weight": 1.5, "fee": 25000, "created_at": "2026-05-01 07:45"},
    {"order_id": "PS005", "customer": "Ha", "area": "Can Tho", "weight": 3.3, "fee": 40000, "created_at": "2026-05-01 11:10"},
    {"order_id": "PS002", "customer": "Long", "area": "Hai Phong", "weight": 7.0, "fee": 70000, "created_at": "2026-05-01 12:00"},
    {"order_id": "PS009", "customer": "Mai", "area": "Da Nang", "weight": 5.5, "fee": 55000, "created_at": "2026-05-01 09:50"},
    {"order_id": "PS004", "customer": "Nam", "area": "Ho Chi Minh", "weight": 2.8, "fee": 35000, "created_at": "2026-05-01 13:25"},
    {"order_id": "PS007", "customer": "Phuong", "area": "Ha Noi", "weight": 8.1, "fee": 80000, "created_at": "2026-05-01 14:30"},
    {"order_id": "PS006", "customer": "Tuan", "area": "Can Tho", "weight": 1.2, "fee": 22000, "created_at": "2026-05-01 15:00"}
]

# Chuyển đổi list dictionary sang Pandas DataFrame
df = pd.DataFrame(orders)

# Chuyển đổi cột 'created_at' sang định dạng datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Hiển thị 5 dòng đầu tiên để kiểm tra
# print(df.head())