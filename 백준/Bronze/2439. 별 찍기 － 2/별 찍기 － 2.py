a = int(input())

for n in range(1,a+1,1):
     for u in range(1,a-n+1,1):
          print(" ",end="")
     for i in range(1,n+1,1):
          print("*",end="")
     print(" ")