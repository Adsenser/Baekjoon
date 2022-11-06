import sys
count = 0
a = int(input())
b = sys.stdin.readline().rstrip().split()
for i in range(a):
    if int(b[i]) == 2:
        count +=1
        continue
    for j in range(2,int(b[i]),1):
        if int(b[i])%j == 0:
            break
        elif j == int(b[i])-1:
            count +=1
print(count)