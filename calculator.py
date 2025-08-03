# simple calculator game where the user inputs two numbers and some calculations are done based on the inputs
print('Howdy! Welcome to my fun calculator')
input('Please press enter to start')
num1 = int(input('Please choose a number: '))
num2 = int(input('Please choose a second number: '))
sum = num1+num2
subtraction = num1 -num2
product = num1*num2
division = num1/num2
print("My super calculator is crunching the numbers ")
input('Please press enter to view your results')

print('The sum of %d and %d is: %d' %(num1,num2,sum))
print('The product of %d and %d is: %d' %(num1,num2,product))
print(' %d substracted from %d is: %d' %(num2, num1, subtraction))
print(' %d divided by %d is: %d' %(num1, num2, division))
print('Thanks for playing!')
input('Please press enter to exit game')

