age=int(input("enter your age: "))
seat=input("did you get seat if yes say enter y: ")

# if age<=10:
#     if seat=="y":
#         print("you bus rent= 100")
#     else:
#         print("your bus rent= 50")
# elif age>10 and age<=19:
#     if seat=="y":
#         print("your rent = 150")
#     else:
#         print("your bus rent = 100")
# elif age>20 and age<=59:
#     if seat=="y":
#         print("your rent =250")
#     else:
#         print("your rent = 200")
# else:
#     if seat=="y":
#         print("your rent = 100")
#     else:
#         print("your rent = 50")

# if age<=10:
#     rent=50
# elif age>10 and age<=19:
#     rent=100
# elif age>20 and age<=59:
#     rent=200
# else:
#     rent=50

# if seat=="y":
#     rent=rent+50

# print(f"your bus rent is {rent}")

if age<=10:
    rent=50
elif 10 < age <=19:
    rent=100
elif 20< age<=59:
    rent=200
else:
    rent=50

if seat=="y":
    rent=rent+50

print(f"your bus rent is {rent}")


