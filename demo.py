def add (a, b, c):
    s1 = a + b 
    # dòng 2 thực hiện 2 phép toán nhưng không làm ảnh hưởng kích thước dữ liệu đầu vào
    s2 = s1 + c
    return s2
# T(n) = 5 => O(1) - thời gian thực hiện không phụ thuộc vào kích thước dữ liệu đầu vào

#  O(n)
def sum (n):
    s = 0
    # dòng 10 thực hiện 1 phép toán
    for i in range(1, n + 1):
    # dòng 12 thực hiện n phép toán
        s += i
    # dòng 14 thực hiện 1 phép toán
    return s
    # dòng 16 thực hiện 1 phép toán
# T(n) = 2n + 1 => O(n) - thời gian thực hiện phụ thuộc vào kích thước dữ liệu đầu vào

# O(n^2)
def sum2 (n):
    s = 0
    # dòng 22 thực hiện 1 phép toán
    for i in range(1, n + 1):
        # dòng 24 thực hiện n phép toán
        for j in range(1, n + 1):
            # dòng 26 thực hiện n phép toán
            s += i * j
    # dòng 28 thực hiện 3 phép toán
    return s
    # dòng 30 thực hiện 1 phép toán
# T(n) = n^2 + n + 1 => O(n^2) - thời gian thực hiện phụ thuộc vào kích thước dữ liệu đầu vào

# O(log n)
def sum3 (n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    return count

# Lưu ý: 
# O(1) rất nhanh
# O(n) duyệt phần tử
# O(n^2) rất dễ gây chậm chương trình
# O(log n) thuật toán cực tốt

# Bài tập: Dùng code hôm trước đã có, hãy tính toán độ phức tạp
