print(tuple(filter(lambda a:a%2==0,range(0,21))))

def is_even(x):
    if x%2==0:
        return True
    else:
        return False
    
l1=list(range(0,21))
print(l1)
l2=list(filter(is_even,l1))
print(l2)
