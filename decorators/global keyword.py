b=30
c=20
def a():
    b=19
    global c
    c=20
    print(b)
    print(c)
    
def d():
    print(b)
    print(c)

a()
d()