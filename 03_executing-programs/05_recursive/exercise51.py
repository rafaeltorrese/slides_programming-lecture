def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    return 1 if n == 1 else n * factorial_iterative(n - 1) 

if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_recursive(5))

    
