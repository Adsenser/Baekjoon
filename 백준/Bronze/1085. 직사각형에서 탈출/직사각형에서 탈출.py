x,y,w,h = map(int,input().split(" "))

if w-x < x:
    a = w-x
elif w-x >= x:
    a = x

if h-y < y:
    b = h-y
elif h-y >= y:
    b = y

if a<b:
    print(a)
elif a>=b:
    print(b)
