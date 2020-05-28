


#  Implement a sum_N_Numbers recursive function to compute the sum of the n natural numbers

#  Note: Natural Numbers start from 1, i.e., 1, 2, 3, 4, 5, …

# Hint : fun(1) = 1 # base case
# fun(n) = fun(n-1) + n # recursive case


def sum_N_Numbers (n):
    if n <= 1:
        return n
    else:
        return n + sum_N_Numbers (n - 1)

print(sum_N_Numbers(5))