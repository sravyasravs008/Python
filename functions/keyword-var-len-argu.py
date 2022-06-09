def cal(*n):
    sum=0
    print(n)
    for x in n:
        sum=sum+x
        
        print(sum)
cal(10,20,40)
cal(10,30)
cal(1,2,3,4,5,6,7)

def cal(**n):
    print(type(n))
    for v in n.values():
        print(v)
        
cal(a=10,b=20,c=30)
cal(a=10,b=20)
cal(a=10)


