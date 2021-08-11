import time


stored_results = {}
def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(1, n + 1)):
        if i in stored_results:
            print(f"Stopping sum at {i} because we have previously computed it")
            result += stored_results[i]
            break
        else:
            result += i
    stored_results[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return result

if __name__ == '__main__':
    print(sum_to_n(1_000_000))
    print(sum_to_n(1_000_000))
