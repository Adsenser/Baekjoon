stairs = int(input())
res_star = 2*stairs-1
star = 1
n=1
for s in range(1,stairs+1):
    for black1 in range(1,(res_star-star)//2+1):
        print(" ",end="")
    for print_star in range(0,2*n-1):
        print("*",end="")
    n +=1  
    star+=2
    if s != stairs:
        print()