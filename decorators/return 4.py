def outer():
    print('hello')
    def d():
        print('gm')
    d()
    d()
outer()
d() #inner wont come when it is return outside 