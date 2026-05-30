import time
import data

# ==========================================
# 1. CÁC HÀM XỬ LÝ TRỰC TIẾP TRÊN DATA ĐƠN HÀNG
# ==========================================

def linear_search_orders(arr, target_customer):
    """Tìm kiếm tuyến tính O(N) theo Tên khách hàng"""
    steps = 0
    for order in arr:
        steps += 1
        if order['customer'].lower() == target_customer.lower():
            return steps # Dừng lại ngay khi tìm thấy
    return steps

def bubble_sort_orders(arr):
    """Sắp xếp nổi bọt O(N^2) theo Giá tiền (fee) tăng dần"""
    steps = 0
    n = len(arr)
    arr_copy = arr.copy() # Tránh làm hỏng data gốc
    
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            # So sánh trường 'fee' của 2 đơn hàng kề nhau
            if arr_copy[j]['fee'] > arr_copy[j + 1]['fee']:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return steps

# ==========================================
# 2. HÀM ĐO THỜI GIAN
# ==========================================

def measure_performance(func, *args):
    """Đo số bước và thời gian chạy"""
    bat_dau = time.perf_counter()
    so_buoc = func(*args)
    ket_thuc = time.perf_counter()
    
    thoi_gian = ket_thuc - bat_dau
    return so_buoc, thoi_gian

# ==========================================
# 3. HÀM IN BÁO CÁO COMPLEXITY
# ==========================================

def print_complexity_report():
    print("\n" + "="*85)
    print(f"{'BÁO CÁO ĐỘ PHỨC TẠP THUẬT TOÁN (TỪ DATA.PY)':^85}")
    print("="*85)
    print(f"{'Thuật Toán':<25} | {'Số Đơn Hàng (N)':<15} | {'Số Bước Chạy':<15} | {'Thời Gian (Giây)':<15}")
    print("-" * 85)

    # Lấy data gốc từ file data.py
    data_goc = data.orders
    
    # Tạo các tập dữ liệu giả lập (nhân bản data gốc lên nhiều lần)
    tap_du_lieu = {
        10: data_goc,                      # 10 đơn hàng (gốc)
        100: data_goc * 10,                # 100 đơn hàng
        500: data_goc * 50,                # 500 đơn hàng
        1000: data_goc * 100               # 1000 đơn hàng
    }

    # Tên khách hàng không có trong danh sách để ép thuật toán chạy hết vòng lặp (Worst-case scenario)
    khach_hang_ao = "KhachHangKhongTonTai"

    for n, arr in tap_du_lieu.items():
        # --- Đo Tìm Kiếm (Tình huống xấu nhất: Tìm khách không tồn tại) ---
        steps_search, time_search = measure_performance(linear_search_orders, arr, khach_hang_ao)
        print(f"{'Linear Search O(N)':<25} | {n:<15} | {steps_search:<15} | {time_search:.6f}")
        
        # --- Đo Sắp Xếp ---
        steps_sort, time_sort = measure_performance(bubble_sort_orders, arr)
        print(f"{'Bubble Sort O(N^2)':<25} | {n:<15} | {steps_sort:<15} | {time_sort:.6f}")
        
        print("-" * 85)

if __name__ == "__main__":
    print_complexity_report()