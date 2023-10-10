def add_num(a,b):
    while b!=0:
        c = a & b
        a = a ^ b
        b = c << 1
    return a
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
sum = add_num(num1,num2)
print('the sum numbers {0} and {1} is {2}'.format(num1,num2,sum))
