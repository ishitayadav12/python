a=5
if(a>3): 
    print("Greater")
elif(a>10):
    print("smaller")
else:
    print("equal to")


# multiple if else statemnets
d=10
if(d==10):
    print("equal")
if(d>5):
    print("Greater")
if(d<15):
    print("Greater")
else:
    print("smaller")

# Solution
age=int(input("age\n "))
if(age<18):
    print("Teenager/Kid")
else:
    print("Adult")

# Logical Operators
age=int(input("Your age: "))
if(age>18 and age<30):
    print("You are eligible")
else:
    print("Sorry, you are not eligible")

marks=int(input("Your marks: "))
if(marks>=50 or marks<= 100):
    print("Pass")
else:
    print("Fail")
