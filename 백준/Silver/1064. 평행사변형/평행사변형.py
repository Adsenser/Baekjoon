import sys
import math
Ax, Ay, Bx, By, Cx, Cy = map(int, sys.stdin.readline().rstrip().split())

length1 = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)
length2 = math.sqrt((Bx - Cx)**2 + (By - Cy)**2)
length3 = math.sqrt((Ax - Cx)**2 + (Ay - Cy)**2)

try:
    if Ax-Bx == 0 and Cx-Bx == 0:
        print(-1)
    elif (Ay-By) / (Ax-Bx) == (Cy-By) / (Cx-Bx):
        print(-1)
    else:
        square1 = (length1 + length2)*2
        square2 = (length2 + length3) * 2
        square3 = (length1 + length3) * 2

        result = max(square1,square2,square3) - min(square1,square2,square3)
        print(result)
except:
    square1 = (length1 + length2) * 2
    square2 = (length2 + length3) * 2
    square3 = (length1 + length3) * 2

    result = max(square1, square2, square3) - min(square1, square2, square3)
    print(result)