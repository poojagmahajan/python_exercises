
# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
# The next number is found by adding up the previous two consecutive numbers.

# fibonacci (0) = 0  # base case
# fibonacci (1) = 1

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))  # recursive case

print(fibonacci(4))
