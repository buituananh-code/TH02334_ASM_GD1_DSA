import data

def menu_sort_orders():
    print("=" * 41)
    print("       MENU SẮP XẾP & LỌC ĐƠN HÀNG       ")
    print("=" * 41)
    print("1. Sắp xếp theo Tên khách hàng (A - Z)")
    print("2. Sắp xếp theo Tên khách hàng (Z - A)")
    print("3. Sắp xếp theo Mã đơn hàng (Order ID)")
    print("4. Sắp xếp theo Thời gian mua hàng (Cũ nhất trước)")
    print("5. Sắp xếp theo Thời gian mua hàng (Mới nhất trước)")
    print("6. Lọc đơn hàng theo Khu vực cụ thể (Khách tự chọn)")
    print("=" * 41)
    
    # Nhận lựa chọn từ người dùng
    luat_chon = input("Nhập lựa chọn của bạn (1-7): ")
    
    # Tạo một bản sao của danh sách đơn hàng để tránh làm xáo trộn dữ liệu gốc trong data.py
    danh_sach_sap_xep = list(data.orders)
    
    # Xử lý sắp xếp và lọc theo từng trường hợp
    if luat_chon == "1":
        danh_sach_sap_xep.sort(key=lambda x: x['customer'])
        print("\n[KẾT QUẢ] Sắp xếp theo Tên khách hàng (A - Z):")
        
    elif luat_chon == "2":
        danh_sach_sap_xep.sort(key=lambda x: x['customer'], reverse=True)
        print("\n[KẾT QUẢ] Sắp xếp theo Tên khách hàng (Z - A):")
        
    elif luat_chon == "3":
        danh_sach_sap_xep.sort(key=lambda x: x['order_id'])
        print("\n[KẾT QUẢ] Sắp xếp theo Mã đơn hàng (Order ID):")
        
    elif luat_chon == "4":
        danh_sach_sap_xep.sort(key=lambda x: x['created_at'])
        print("\n[KẾT QUẢ] Sắp xếp theo Thời gian mua hàng (Cũ nhất trước):")
        
    elif luat_chon == "5":
        danh_sach_sap_xep.sort(key=lambda x: x['created_at'], reverse=True)
        print("\n[KẾT QUẢ] Sắp xếp theo Thời gian mua hàng (Mới nhất trước):")
        
    elif luat_chon == "6":
        # Yêu cầu người dùng nhập tên khu vực muốn xem
        ten_khu_vuc = input("Nhập tên khu vực bạn muốn tìm (VD: Ha Noi, Da Nang...): ")
        
        # Dùng List Comprehension để lọc ra các đơn hàng khớp với khu vực vừa nhập
        danh_sach_sap_xep = [order for order in danh_sach_sap_xep if ten_khu_vuc.lower() in order['area'].lower()]
        print(f"\n[KẾT QUẢ] Các đơn hàng tại khu vực '{ten_khu_vuc}':")
        
        # Nếu nhập sai tên khu vực hoặc không có đơn hàng nào
        if len(danh_sach_sap_xep) == 0:
            print("Không tìm thấy đơn hàng nào ở khu vực này!")
            return
            
    else:
        print("\nLựa chọn không hợp lệ! Vui lòng chạy lại chương trình.")
        return

    # In kết quả ra màn hình
    print("=" * 75)
    for order in danh_sach_sap_xep:
        print(f"Mã ĐH: {order['order_id']} | Khách: {order['customer']:<6} | Khu vực: {order['area']:<12} | Thời gian: {order['created_at']}")
    print("=" * 75)

# Chạy hàm menu khi bấm run file sort_tools.py
if __name__ == "__main__":
    menu_sort_orders()