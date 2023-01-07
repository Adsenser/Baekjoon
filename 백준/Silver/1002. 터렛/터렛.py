import sys
import math
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().rstrip().split())
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if max(r1,r2) > distance:
        if x1==x2 and y1==y2 and r1==r2:
            print(-1)
        elif min(r1,r2) + distance == max(r1,r2):
            print(1)
        elif min(r1,r2) + distance > max(r1,r2):
            print(2)
        else:
            print(0)
    elif max(r1,r2) == distance:
        print(2)
    else:
        if distance < r1+r2:
            print(2)
        elif distance == r1+r2:
            print(1)
        else:
            print(0)
