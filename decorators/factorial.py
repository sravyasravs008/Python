def fac(n):
    i=1
    while n>=1:
        i=i*n
        n=n-1
    return i

result=fac(3)
print(result)