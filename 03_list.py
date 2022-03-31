l1=[1,3,5,7,45,67,89,23,0,73]
print(l1)
l1.sort()
print("Sorted list" , l1)
l1.reverse()
print("Reverse list" , l1)
l1.append(90)
l1.append(56)
l1.append(2)
print("Modified list", l1)
l1.insert(2, 5)
print("Rectified list", l1)
l1[4]=99
print(l1)

# soultion 1
a=input("fruit 1 \t")
b=input("fruit 2 \t")
c=input("fruit 3 \t")
d=input("fruit 4 \t")
e=input("fruit 5 \t")
f=input("fruit 6 \t")
g=input("fruit 7 \t")

list=[a,b,c,d,e,f,g]
print(list)

# solution2

a=int (input("mark1 \t"))
b=int (input("mark2 \t"))
c=int (input("mark3 \t"))
d=int (input("mark4 \t"))
e=int (input("mark5 \t"))
f=int (input("mark6 \t"))
g=int (input("mark7 \t"))
result=[a,b,c,d,e,f,g]
print("Discrete result", result)
result.sort()
print("Sorted Result", result)