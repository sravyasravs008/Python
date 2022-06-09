d={'id':202,'name':'sss'}
print(d['id'])
print(d['name'])
d['name']='ddd'
d['sal']=45000
print(d)
for x in d:
    print(x)


d={'id':202,'name':'ddd'}
print(d['id'])
print(d['name'])
d['name']='ffff'
d['sal']=3000
print(d)
for s in d:
    print(d[s])
    
emp={'id':202,'name':'vvv','sal':30000}
for x in emp:
    print(x, "=",emp[x])
    