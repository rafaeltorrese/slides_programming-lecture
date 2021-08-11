x = 4
def myfunc():
    x = 10
    def inner():
        nonlocal x
        print(x)
    inner()
myfunc()