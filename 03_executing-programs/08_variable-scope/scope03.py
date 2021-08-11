total = 0
def add_to_total(n):
    global total
    total = total + n

if __name__ == '__main__':
    add_to_total(5)
    print(total)
