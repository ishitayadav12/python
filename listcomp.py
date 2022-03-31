a=[2,4,3,7,5,9,8,6,0]
b=[]
for item in a :
    if item%2 == 0:
        b.append(item)

print(b)

# or other way using list comprehension
c=[item for item in a if item%2==0]
print(c)


# solution
n=int(input("Enter number for table: "))
table=[n*i for i in range (1,11)]
print(table)


    

