d=int(input('enter no of employes:'))
emp={}
i=0
while i<=d:
    a=input('enter employes')
    b=int(input('enter salary'))
    emp[a]=b
    i=i+1
    print(emp)
for k in emp:
    print(k,"=",emp[k])
    