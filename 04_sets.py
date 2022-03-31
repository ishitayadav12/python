a={1,2,3,4,5,1}
print(a)
print(type(a))

d={}
print(type(d))
# empty dictionary

b=set()
print(type(b))
# empty set
b.add(4)
b.add(6)
print(b)

e=([4,5])
print(e)
b.add((9,0))     #tupple  hashsable
print(b)
#b.add({6:8})     #dictionary  unhashable
#print(b)
#b.add([5,2])     #list unhashable
print(len(b))
b.remove(4)
print(b)
print(len(e))

b.pop()           #removes arbitrary element from set
print(b)

b.intersection({6,9})
print(b)

b.union({6,9})

# solution 2
num1=int(input("Enter num 1 \n"))
num2=int(input("Enter num 2 \n"))
num3=int(input("Enter num 3 \n"))
num4=int(input("Enter num 4 \n"))
num5=int(input("Enter num 5 \n"))
num6=int(input("Enter num 6 \n"))
num7=int(input("Enter num 7 \n"))
num8=int(input("Enter num 8 \n"))

s={ num1, num2,num3, num4, num5, num6, num7, num8}
print(s)


