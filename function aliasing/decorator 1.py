def outer():
    
    def inner():
        print('Inner function')
        
    inner()
        
outer()

def outer():
    print('hello')
outer()
print(id(10))
a=outer
a()
        