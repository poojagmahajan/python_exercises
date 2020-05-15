

# recursion is when function call itself again and again till reaches to base condition.

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n * factorial(n-1))   # call fun factorial again

print("Factorial:")
print(factorial(5))