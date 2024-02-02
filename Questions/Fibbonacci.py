# def fibonacci_recursive(n):
#     if n <= 1:
#         return [0] if n == 0 else [0, 1]

#     fib_series = fibonacci_recursive(n - 1)
#     fib_series.append(fib_series[-1] + fib_series[-2])

#     return fib_series

# # Example: Print the first 10 Fibonacci numbers
# n=int(input("Enter the number"))
# result = fibonacci_recursive(n)
# print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibb(n):
    if n <= 1:
        if n == 0:
            result = [0]
        else:
            result = [0, 1]
    else:
        fibb_series = fibb(n-1)
        fibb_series.append(fibb_series[-1] + fibb_series[-2])
        result = fibb_series
    return result

result = fibb(10)
print(result)
