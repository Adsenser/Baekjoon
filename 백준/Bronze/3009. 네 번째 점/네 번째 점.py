ax, ay =map(int,input().split(" "))
bx, by =map(int,input().split(" "))
cx, cy =map(int,input().split(" "))

if ax == bx:
    dx = cx
else:
    if ax == cx:
        dx = bx
    else:
        dx = ax

if ay == by:
    dy = cy
else:
    if ay == cy:
        dy = by
    else:
        dy = ay

print("%d %d" % (dx, dy))
