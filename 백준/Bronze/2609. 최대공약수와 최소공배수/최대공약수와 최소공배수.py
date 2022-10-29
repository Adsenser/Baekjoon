a,b = map(int,input().split(" "))
c = [a,b]
n = 1
while True:
    if a%n ==0 and b%n ==0:
        max = n
        aa = a//n
        bb = b//n
        n += 1
    else:
        if n >= min(c):
            break
        n += 1
print(max)
print(max*aa*bb)
