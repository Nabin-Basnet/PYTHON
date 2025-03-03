# Python Conditions and If statements
a=20
b=30

if a>b :
    print("true")
else:
    print("false")

print("a is greater") if a>b else print("bis greater")
print("A") if a > b else print("=") if a == b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# if statements cannot be empty, but if you for 
# some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.
if b > a:
  pass