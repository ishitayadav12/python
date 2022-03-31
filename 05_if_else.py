# solution1
a=int(input("Number1: \n"))
b=int(input("Number2: \n"))
c=int(input("Number3: \n"))
d=int(input("Number4: \n"))

if(a>=b and a>=c and a>=d):
    print(f"{a} is Greatest")
elif(b>=a and b>=c and b>=d):
    print(f" {b} is greatest")
elif(c>=a and c>=b and c>=d):
    print(f" {c} is Greatest")
else:
    print(d, "Greatest is")

# solution2
 
m1=int(input("Enter marks for Subject1:\n"))
m2=int(input("Enter marks for Subject2:\n"))
m3=int(input("Enter marks for Subject3:\n"))
avg=(m1+m2+m3)/3

if(m1<33 or m2<33 or m3<33):
    print("You are fail because of 1 subject")
elif(avg<40):
    print("FAIL because of overall % ")
else:
    print("PASS")

# solution3
# spam detector
text= input("Enter the text:\n")
if("money" in text):
    print("spam")
elif("buy now"in text):
    print("spam")
elif("discount offer" in text):
    print("Spam")
else:
    print("Not a Spam")

# solution 4
username=input("Enter your username: \n")
if(len(username)<10):
    print("Eligible")
else:
    print("Not Eligible")

# solution 5
marks=int(input("Enter your marks: \n"))
if(marks>=90 and marks<=100):
    print("Excellent: O+")
elif(marks>=80 and marks<90):
    print("A+")
elif(marks>=70 and marks<80):
    print("B+")
elif(marks>=60 and marks<50):
    print("C+")
else:
    print("Fail")
