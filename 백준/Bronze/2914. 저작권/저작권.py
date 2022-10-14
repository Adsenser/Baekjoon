import math
a,b = map(int,input().split(" "))
b2 = b-0.99999
result = a*b2
print(math.ceil(result))