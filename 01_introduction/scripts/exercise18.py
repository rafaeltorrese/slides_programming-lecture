if __name__ == "__main__":
    
    number = abs(int(input("Enter a number to see if it's a perfect square: " )))
    i = -1
    square = False
    while i <= number ** 0.5:
        i += 1
        if i * i == number:
            square = True
            break
    if square:
        print(f"The square root of {number} is {i}")
    else:
        print(f"{number} is not a perfect square")
    
