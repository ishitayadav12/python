# solution
from functools import reduce

# maxy = lambda a,b : max(a,b)
maxlist = [56,78,23,56,34,35,90,100]
# print(reduce(maxy, maxlist))
print(reduce(max, maxlist))
