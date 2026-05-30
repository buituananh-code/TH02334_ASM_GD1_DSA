import data
import search_tools
import sort_tools
import complexity_report

def hien_thi_toan_bo_don_hang():
    """Hàm phụ để in toàn bộ dữ liệu cho người dùng xem trước"""
    print("\n" + "-" * 75)
    print(f"{'MÃ ĐH':<8} | {'KHÁCH HÀNG':<12} | {'KHU VỰC':<15} | {'CƯỚC PHÍ':<10} | {'THỜI GIAN'}")
    print("-" * 75)
    for o in data.orders:
        print(f"{o['order_id']:<8} | {o['customer']:<12} | {o['area']:<15} | {o['fee']:<10} | {o['created_at']}")
    print("-" * 75)

def main_menu():
    while True:
        print("\n" + "="*60)
        print("    CHƯƠNG TRÌNH QUẢN LÝ ĐƠN HÀNG - POLY-SHIP")
        print("    Made by: KETA")
        print("="*60)
        print("1. Hiển thị toàn bộ danh sách đơn hàng")
        print("2. Tìm kiếm đơn hàng (Theo Tên Khách Hàng)")
        print("3. Sắp xếp và Lọc đơn hàng")
        print("4. Xuất Báo cáo Độ phức tạp Giải thuật (Complexity Report)")
        print("0. Thoát chương trình")
        print("="*60)

        chon = input("Vui lòng chọn chức năng (0-4): ")

        if chon == "1":
            hien_thi_toan_bo_don_hang()
            
        elif chon == "2":
            tu_khoa = input("\nNhập tên khách hàng cần tìm: ")
            # Gọi hàm tìm kiếm từ file search_tools.py
            ket_qua = search_tools.search_orders_by_customer(data.orders, tu_khoa)
            
            if ket_qua:
                print(f"\n[KẾT QUẢ] Tìm thấy {len(ket_qua)} đơn hàng:")
                for o in ket_qua:
                    print(f"Mã ĐH: {o['order_id']} | Khách: {o['customer']:<6} | Khu vực: {o['area']}")
            else:
                print(f"\nKhông tìm thấy khách hàng nào tên '{tu_khoa}'!")
                
        elif chon == "3":
            # Gọi nguyên cái menu sắp xếp từ file sort_tools.py sang
            sort_tools.menu_sort_orders()
            
        elif chon == "4":
            # Gọi hàm in báo cáo từ file complexity_report.py
            complexity_report.print_complexity_report()
            
        elif chon == "0":
            print("\nCảm ơn thầy và các bạn đã sử dụng chương trình.\nDonate: 2112132270 - BIDV - Bui Tuan Anh (˶ᵔ ᵕ ᵔ˶)")
            break
            
        else:
            print("\nLựa chọn không hợp lệ, vui lòng nhập lại (từ 0 đến 4)!")

if __name__ == "__main__":
    main_menu()