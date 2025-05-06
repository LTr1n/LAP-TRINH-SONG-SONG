import pandas as pd
import multiprocessing

def bubble_sort(arr):
    """ Thuật toán Bubble Sort cơ bản (sắp xếp tăng dần theo cột Marks) """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][2] > arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def process_sort(chunk):
    """ Hàm thực thi Bubble Sort trên một phần dữ liệu """
    return bubble_sort(chunk)

def merge_sorted_chunks(chunks):
    """ Hợp nhất các phần dữ liệu đã sắp xếp """
    merged = []
    for chunk in chunks:
        merged.extend(chunk)
    return sorted(merged, key=lambda x: x[2])  # Sắp xếp lại toàn bộ dữ liệu theo Marks

def parallel_bubble_sort(data, num_processes=4):
    """ Sắp xếp song song bằng Multiprocessing """
    size = len(data)
    chunk_size = size // num_processes
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes - 1)]
    chunks.append(data[(num_processes - 1) * chunk_size:])
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(process_sort, chunks)
    
    # Hợp nhất kết quả đã sắp xếp
    sorted_data = merge_sorted_chunks(sorted_chunks)
    return sorted_data

if __name__ == "__main__":
    file_path = "Student_Marks.csv"
    output_path = "Sorted_Parallel.csv"

    try:
        df = pd.read_csv(file_path)
        data_list = df.values.tolist()

        # Thực hiện sắp xếp song song bằng Multiprocessing
        sorted_result = parallel_bubble_sort(data_list, num_processes=4)

        # Chuyển kết quả thành DataFrame
        sorted_df = pd.DataFrame(sorted_result, columns=df.columns)

        # Lưu kết quả vào file CSV
        sorted_df.to_csv(output_path, index=False)

        print(f"Sắp xếp hoàn tất! Kết quả được lưu vào {output_path}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")