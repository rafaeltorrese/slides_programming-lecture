def countdown(n):
    if n == 0:
        print("liftoff!")
    else:
        print(n)
        return countdown(n - 1)

if __name__ == '__main__':
    countdown(3)