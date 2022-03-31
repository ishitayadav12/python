def square(num):
    return num*num

l1 = [1,2,4,6]
l2 = []
# method1
for item in l1:
    l2.append(square(item))
print(l2)

# method2
print(list(map(square,l1)))

# map function 
divide = lambda x: x/5
l=[25, 10, 16]
print(list(map(divide, l)))

# filter function
divide = lambda x: x%5==0
l=[25, 10, 16, 90, 83, 67]
print(list(filter(divide, l)))




