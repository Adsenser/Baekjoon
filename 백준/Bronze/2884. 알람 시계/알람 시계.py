t, m = map(int,input().split(" "))

if t == 0:
     if m-45<0:
          m = m+60-45
          t = 23
     else:
          m = m-45
else:
     if m-45<0:
          m = m+60-45
          t = t-1
     else:
          m = m-45

print(t,m)