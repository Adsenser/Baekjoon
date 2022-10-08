people, width = map(int,input().split(" "))
a,b,c,d,e = map(int,input().split(" "))
sang = people*width
print("%d %d %d %d %d" % (a-sang,b-sang,c-sang,d-sang,e-sang))