if __name__ == "__main__":
    num1, num2 = 24, 36
    iterator = 1
    while True:
        if not (iterator % num1) and not (iterator % num2):
            break
        iterator += 1
        
    print(f'The LCM of {num1} and {num2} is {iterator}')
