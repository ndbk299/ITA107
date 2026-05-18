#  tính giai thừa
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    else:
        # recursive case
        return n * factorial(n - 1)
n = int(input("Nhập n: "))
print(f"Giai thừa của {n} là: {factorial(n)}")

# đệ quy
def factorial_recursive(n):
    # base case
    if n == 0 or n == 1:
        return 1
    else:
        # recursive case
        return n * factorial_recursive(n - 1)
n = int(input("Nhập n: "))
print(f"Giai thừa của {n} là: {factorial_recursive(n)}")

# tính dãy Fibonacci ( thường và đệ quy)
# thường 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Nhập n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")

# đệ quy
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Nhập n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci_recursive(n)}")
