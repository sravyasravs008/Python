from functools import*
result=reduce(lambda a,b:a+b,[10,20,30,40])
print(result)

s=reduce(lambda a,b:a-b,[50,40,3,2])
print(s)

s=reduce(lambda a,b:a*b,[20,30])
print(s)

d=reduce(lambda a,b:a//b,[30,5])
print(d)

