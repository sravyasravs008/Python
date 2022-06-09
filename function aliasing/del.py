def s():
    print('hello')
a=s #function aliasing
a()
s()
del s
a()
s()