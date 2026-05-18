# Bài 1:
print("\nBài 1:")

# Nhập từ bàn phím 1 số
n = int(input("Nhập một số: "))

# Kiểm tra và hiện thị ra màn hình số đó là chẵn hay lẻ
if n % 2 == 0:
    print(f"{n} là số chẵn.")
else:    print(f"{n} là số lẻ.")

# Bài 2:
print("\nBài 2:")

# Nhập vào 1 số 
n = int(input("Nhập một số: "))

# Kiểm tra xem số dưới những yêu cầu sau:

# - Có phải số nguyên tố hay không?
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
prime_status = "là số nguyên tố" if is_prime(n) else "không phải là số nguyên tố"
print(f"{n} {prime_status}.")

# - Có phải số chính  phương hay không?
def is_perfect_square(num):
    return int(num**0.5)**2 == num
square_status = "là số chính phương" if is_perfect_square(n) else "không phải là số chính phương"
print(f"{n} {square_status}.")

# - Có phải số hoàn hảo hay không?
def is_perfect_number(num):
    if num < 2:
        return False
    sum_of_divisors = sum( i for i in range(1,num) if num % i == 0)
    return sum_of_divisors == num
perfect_status = "là số hoàn hảo" if is_perfect_number(n) else "không phải là số hoàn hảo"
print(f"{n} {perfect_status}.")

# Bài 3: 
print("\nBài 3:")   

# - Nhập vào 1 mảng số 
array = list(map(int, input("Nhập một mảng số (cách nhau bằng dấu cách): ").split()))

# Tìm ra các số chính phương và nguyên tố
perfect_squares = [x for x in array if is_perfect_square(x)]
primes = [x for x in array if is_prime(x)]
print(f"Các số chính phương trong mảng: {perfect_squares}")
print(f"Các số nguyên tố trong mảng: {primes}")
