# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x=lambda a:a+10

print(x(6))

# Lambda functions can take any number of arguments:
sum=lambda a,b:a+b
print("sum using lambda function " ,sum(4,5))

summ=lambda a,b,c:a+b+c
print(summ(3,5,7))
