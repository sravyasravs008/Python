def outer():
    print('outer function')
    def inner():
        print('inner function')
    return inner
    
outer()
a=outer()
print(a())
print(a)
a()