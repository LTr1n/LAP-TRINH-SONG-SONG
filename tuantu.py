import pandas as pd

def bubble_sort(arr):
    """ Thuật toán Bubble Sort cơ bản (tuần tự) """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][2] > arr[j + 1][2]:  # Sắp xếp theo cột Marks (cột thứ 3)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    file_path = "/Users/macbook/Desktop/Hoc tap/Lập trình tính toán song song/Student_Marks.csv"

    try:
        df = pd.read_csv(file_path)
        data_list = df.values.tolist()

        # Thực hiện sắp xếp tuần tự
        sorted_result = bubble_sort(data_list)

        # Chuyển kết quả thành DataFrame
        sorted_df = pd.DataFrame(sorted_result, columns=df.columns)

        # Lưu kết quả vào file CSV
        sorted_df.to_csv("/Users/macbook/Desktop/Hoc tap/Lập trình tính toán song song/Sorted.csv", index=False)

        print("Sắp xếp hoàn tất! Kết quả được lưu vào Sorted.csv")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
