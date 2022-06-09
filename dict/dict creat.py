emp={'sss':45000,'ddd':5000}
d=dict([('id',202),('name','ddd'),('sal',4000)])
print(len(emp))
print(emp.get('ddd'))
print(emp.values())
print(d.items())


emp={'sravya':60000,'ddd':40000,'fff':40000}
print(len(emp))
print(emp.get('ddd'))
print(emp.keys())
print(emp.items())
for k,v in emp.items():
    print(k,'=',v)