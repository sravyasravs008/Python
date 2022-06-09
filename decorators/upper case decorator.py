def upper(func):
    def inner():
        return func().lower()
    return inner
@upper
def low():
    return'hello world'
print(low())




def upper(func):
    def inner():
        return func().upper()
    return inner
@upper
def low():
    return 'hello world'
print(low())