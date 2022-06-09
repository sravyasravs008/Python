def num(a):
    if a%3==0:
        return True
    else:
        return False
l1=[10,20,30,6,9]

l2=list(filter(num,l1))
print(l1)
print(l2)