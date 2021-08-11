def sum_first_n(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

if __name__ == '__main__':
    print(sum_first_n(100))