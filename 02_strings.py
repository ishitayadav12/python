# use of single, double and tripple inverted commas for strings
a='Ishita'
print(a)
a="Ishita"
print(a)
a='''Ishita'''
print(a)
a="Ishita's"
print(a)
a='''Ishita's and Ishita"s'''
print(a)
a=''' Ishita's and 
        Ishita"sfdc'''
print(a)

# concatenating two strings
a="Goodmorning,"
b="Ishita"
c=a+b
print(c)

name="Ishita"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[1:4])
print(name[0:4])
print(name[2:3])
print(name[4:])
print(name[:4])
print(name[1:])
print(name[5: ])

name="computerscienceengineering"
d=name[2:4]
d=name[2::8]
print(d)

# string functions
string= '''Our example paragraph will be about human misconceptions of piranhas where Decide on a controlling idea and create a topic sentence the Paragraph'''
print(len(string))
print(string.endswith("Paraghraph"))
print(string.count(a))
print(string.count("paraghraph"))
print(string.find("where"))
print(string.find("our"))
print(string.find("example"))
print(string.find("misconception"))
print(string.replace("Our", "your"))


# solution 1
string="Goodmorning, Welcome "
a=input("Enter name \n")
c= string + a 
print(c)  #print(string, a)