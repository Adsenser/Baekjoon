t = int(input())
a,b,c = 0,0,0

if t%10 != 0:
    print(-1)
else:
    if t//300 != 0:
        a = t//300
    if (t%300)//60 != 0:
        b = (t%300)//60
    if (t%300)%60//10 != 0:
        c = (t%300)%60//10

    print("%d %d %d" % (a,b,c))