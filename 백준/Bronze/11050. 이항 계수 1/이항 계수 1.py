a, b = map(int,input().split(" "))
up = 1
for _ in range(b):
    up *= a
    a -=1

down = 1
for _ in range(b):
    down *= b
    b -= 1

print(int(up/down))