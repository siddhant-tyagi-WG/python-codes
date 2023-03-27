def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Generate the first 10 Fibonacci numbers
fib = fibonacci_generator(10)
print(fib)
print(list(fib))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

