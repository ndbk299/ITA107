# def snippet_1(n):
#     total = 0 # 1 phép gán
#     for i in range(n): # lặp n lần
#         total = total + 1 
#     return total    
# # Độ phức tạp: O(n)
# # Giải thích: vòng for chạy n lần, mỗi lần chỉ có 1 phép gán/cộng.

# def snippet_2(n):
#     count = 0  # 1 phép gán
#     for i in range(n): # lặp n lần
#         for j in range(n): # lặp n lần
#             count += 1
#     return count
# # Độ phức tạp: O(n^2)
# # Giải thích: có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2 bước.

# def snippet_3(n):
#     steps = 0 # 1 phép gán
#     while n > 0: 
#         n = n // 2 # chia n cho 2
#         steps += 1 
#     return steps
# # Độ phức tạp: O(log n)
# # Giải thích: mỗi vòng lặp chia n cho 2 nên số bước là log2(n)

# def constant_work():
#     x = 1
#     y = 2
#     z = x + y
#     return z

# def snippet_4(n):
#     for i in range(n):
#         constant_work()
# # Độ phức tạp: O(n)
# # Giải thích: vòng for chạy n lần, mỗi lần gọi hàm O(1), nên tổng thời gian tỉ lệ tuyến tính với n.

# def snippet_5(n):
#     total = 0
#     for i in range(n):
#         for j in range(i):
#             total += 1
#     return total
# # Độ phức tạp: O(n^2)
# # Giải thích: có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2 bước.

# def snippet_6(n):
#     k = 1
#     total = 0
#     while k < n:
#         for i in range(n):
#             total += 1
#         k = k * 2
#     return total
# # Độ phức tạp: O(n log n)
# # Giải thích: vòng while chạy log n lần, mỗi lần vòng for chạy n lần → tổng n * log n = n log n bước.

# def snippet_7(arr):
#     count = 0
#     for x in arr:
#         if x in arr: # kiểm tra x có trong arr
#             count += 1
#     return count
# # Độ phức tạp: O(n^2)
# # Giải thích: vòng for chạy n lần, mỗi lần kiểm tra x có trong arr hay không → tổng n * n = n^2 bước.

# def snippet_8(arr):
#     s = set(arr)
#     count = 0
#     for x in arr:
#         if x in s:
#             count += 1
#     return count
# # Độ phức tạp: O(n)
# # Giải thích: chuyển mảng thành tập hợp (set) để kiểm tra sự tồn tại của phần tử trong thời gian O(1), sau đó duyệt qua mảng một lần → tổng n * 1 = n bước.

def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
# Độ phức tạp: O(n^2)
# Giải thích: có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2 bước

def two_sum_linear(arr, target):
    seen = {}  # key: giá trị, value: chỉ số
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return (seen[complement], i)
        seen[arr[i]] = i
    return None
# Độ phức tạp: O(n)
# Giải thích: duyệt 1 lần qua mảng, mỗi bước kiểm tra và thêm vào dict đều O(1).
