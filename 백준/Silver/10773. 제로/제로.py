import sys
k = int(input())
a = []
for i in range(k):
    data = int(sys.stdin.readline().rstrip())
    if data != 0:
        a.append(data)
    else:
        a.pop()
sum = 0
for j in a:
    sum += j
print(sum)