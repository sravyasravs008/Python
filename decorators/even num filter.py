def a(num):
    if num % 2 == 0:
        return True
    else:
        return False
l1 = [1,2,3,4,5,6,7,8,9]
x=filter(a,l1)
print(x)
l2=list(filter(a,l1))
print(l1)
print(l2)

#odd number

def a(num):
    if num%2!=0:
        return True
    else:
        return False  
l1=[1,2,3,4,5,67]
x=filter(a,l1)
print(x)
l2=list(filter(a,l1))
print(l1)
print(l2)