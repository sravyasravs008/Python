def is_odd(num):
    if num%3!=0:
        return True
    else:
        return False
l1=(1,3,4,5,6,7,9)
l2=list(filter(is_odd,l1))
print(l1)
print(l2)