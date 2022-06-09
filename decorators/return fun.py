def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner
innerfun=outer
innerfun=outer()
innerfun()
innerfun()
