x = "Hello, World"

def func():
    x = 2
    print(f"Inside 'func', x has the value {x} ")

if __name__ == '__main__':
    func()
    print(f"Outside 'func', x has the value {x}")