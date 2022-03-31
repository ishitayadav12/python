letter= ''' Dear <name> ,
Greetings from ABC Clubhouse. We are happy to inform you that you have been selected!
Thanks and Regards, 
Bill
Date= DATE '''

name=input("Enter your name \n")
date=input("Enter the date \n")
letter= letter.replace("<name>" , name)
letter= letter.replace("DATE", date)
print(letter)

# solution 4
str="This is a sample string to detect double  spaces"
twospaces=str.find("  ")
print(twospaces)
singlespace=str.replace("  "," ")
print(singlespace)

