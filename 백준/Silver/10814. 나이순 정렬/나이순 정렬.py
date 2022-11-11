n = int(input())
a = []
for i in range(n):
    b = list(input().split())
    b.append(i)
    a.append(b)

a.sort(key=lambda x:int(x[0]))

for j in range(n):
    print(int(a[j][0]),a[j][1])

