emp={'hh':456,'dd':'hh','sal':4567}
removed_item=emp.pop('hh')
print(emp)
print(removed_item)

emp.popitem()
print(emp)
emp.clear()
print(emp)