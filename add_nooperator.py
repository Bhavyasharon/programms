def add_num(a,b):
    if a!= b:
        return (a*a - b*b)/(a-b)
    else:
        return 2*a
num1 = int(input('enter first number:'))
num2 = int(input("enter second number: "))
sum = add_num(num1,num2)
print('{0} + {1} = {2}'.format(num1,num2,sum))

