n,k = map(int,input().split())
a= []
result = []
for i in range(1,n+1,1):
    a.append(i)
b = k
for _ in range(0,len(a)):
    if b > len(a):
        while b > len(a):
            b = b - len(a)
    result.append(a[b-1])
    del(a[b-1])
    b += k-1
print("<",end="")
for i in range(len(result)):
    if i != len(result)-1:
        print(result[i],end=", ")
    else:
        print(result[i],end=">")