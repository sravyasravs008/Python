l1=[1,2,3,4,5]
def a(x):
    return x+1
#l2=list(map(a,l1))
l2=list(map(lambda x:x+1,l1))
print(l2)
print(l1)