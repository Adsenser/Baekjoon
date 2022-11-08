import sys
a = int(input())
c = []
for i in range(a):
    b = int(sys.stdin.readline().rstrip())
    c.append(b)

c.sort()

for j in range(len(c)):
    print(c[j])