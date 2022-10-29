a = str(input())
if int(a) < 10:
    a = '0'+str(a)
aa = a[:]
count = 0
while True:
    b = int(a[0]) + int(a[1])
    if b < 10:
        c = '0'+str(b)
    else:
        c = str(b)
    count += 1
    a = a[1] + c[1]
    if a == aa:
        break
print(count)