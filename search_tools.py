import data

def search_orders_by_customer(orders, query):
    return [order for order in orders if query.lower() in order['customer'].lower()]

# Tìm kiếm
# gia_tri_tim_kiem = search_orders_by_customer(data.orders, "Tuan")

# Kiểm tra xem có tìm thấy hay không và in xuống dòng
# if gia_tri_tim_kiem:
#     for order in gia_tri_tim_kiem:
#         print("=== THÔNG TIN ĐƠN HÀNG ===")
#         for key, value in order.items():
#             print(f"{key}: {value}")
#         print("=" * 26)
# else:
#     print("Không tìm thấy kết quả nào!")