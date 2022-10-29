
a,b = list(map(str,input().split(" ")))
aa = a[::-1]
bb = b[::-1]
aaa = 0
bbb = 0
for i in range(1,len(aa)+1):
    aaa += int(aa[-i])*(10**(i-1))
for j in range(1,len(bb)+1):
    bbb += int(bb[-j])*(10**(j-1))

if aaa < bbb:
    print(bbb)
else:
    print(aaa)

