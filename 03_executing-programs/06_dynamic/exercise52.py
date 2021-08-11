stored_results = {}
def sum_to_n(n):
    result = 0
    for i in reversed(range(1, n + 1)):
        if i in stored_results:
            print(f"Stopping sum at {i} because we have previously computed it")
            result += stored_results[i]
            break
        else:
            result += i
    stored_results[n] = result
    return result

if __name__ == '__main__':
    print(sum_to_n(5))
    print(sum_to_n(6))
