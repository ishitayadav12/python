i=1
while i<=50:
    print(i)
    i=i+1
print("\n")
for j in range(10):
    print(j)
print("\n")
for j in range(5,10):
    print(j)

# solution1
num=int(input("user enter the number: \n"))
for i in range (11):
    print(str(num)+ "X"+ str(i)+ "=" + str(i*num))

# solution 2

num=int(input("user enter the number: \n"))
factorial=1
for i in range (i , num+1):
    factorial=factorial*i
print(f"{factorial}")