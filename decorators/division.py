def simple_div(func):
    def inner(a,b,c):
        if b==2:
            print('add')
        else:
            return func(a,b,c)
    return inner
@simple_div
def add(a,b,c):
    return a+b+c
print(add(10,20,30))
add(10,2,3)
        