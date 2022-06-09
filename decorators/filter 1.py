
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
l1=[10,20,304,47,50,39]
x=filter(is_even,l1)
print(x)
l2=list(filter(is_even,l1))
print(l1)
print(l2)


    
