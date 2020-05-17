x = float(input('Enter the first value:'))
y = float(input('Enter the second value:'))

z = input('Enter the operation (+,-,*,/):')

if z=='+':
    print('You have chosen to perform + and the result is',x+y)
elif z=='-':
    print('You have chosen to perform - and the result is',x-y)
elif z=='*':
    print('You have chosen to perform * and the result is', x*y)
elif z=='/':
    print('You have chosen to perform / and the result is',x/y)
else:
    print('you have chosen the wrong operation.')