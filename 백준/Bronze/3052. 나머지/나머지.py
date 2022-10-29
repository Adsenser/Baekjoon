a = []
for _ in range(10):
    a.append(int(input()))
b = []
for i in range(len(a)):
    tmp = a[i] % 42
    b.append(tmp)
b.sort()
count = 1
for j in range(len(b)-1):
    if b[j] != b[j+1]:
        count +=1

print(count)