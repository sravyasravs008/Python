emp={'id':202,'name':'ss','sal':4000}
print(emp.get('id'))
print(emp.get('loc'))
print(emp.get('loc','switz'))

print(emp.keys)
for k in emp.keys():
    print(k)
    
print(emp.values())
for s in emp.values():
    print(s)
    
print(emp.items())
    