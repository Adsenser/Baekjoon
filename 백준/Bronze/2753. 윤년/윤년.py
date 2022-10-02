y = int(input())
yy = 0

if y%4 == 0:
     if y%400 ==0:
          yy = 1
     elif y%100 ==0:
          yy = 0
     else:
          yy =1
else:
     yy = 0

print(yy)