'''
def employe(name):
    print('hello',name,'gm')
employe('ss')
employe('dd')
employe('ff')
'''
def name(a):
    def inner(name):
        if name=='modi':
            print('hello,pm,gm')
        else:
            a(name)
    return inner
@name
def employe(name):
    print('hello',name,'gm')
employe('rahul')
employe('modi')
employe('sonia')

