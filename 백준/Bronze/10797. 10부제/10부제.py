day = int(input())
a,b,c,d,e = map(int,input().split(" "))
count = 0
if a == day:
    count +=1
if b == day:
    count +=1
if c == day:
    count +=1
if d == day:
    count +=1
if e == day:
    count +=1
print(count)