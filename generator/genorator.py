a=3
print(type(a))
def genrate_months():
    print('generating months')
    yield 'jan'
    yield 'feb'
    yield 'mar'
    yield 'apr'
g=genrate_months()
print(g)
for x in g:
    print(x)