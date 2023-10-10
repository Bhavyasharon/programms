def add_num(a,b):
    sum = a + b
    return sum
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
sum = num1 + num2
print('the sum of numbers {0} and {1} is {2}'.format(num1,num2,add_num(num1,num2)))
