a= int(input('enter first number'))
b= int(input('enter second number'))
c= int(input('enter third number'))
min= a if a<b and b>c else b if b<c and b>c else c
print(bool('min'))