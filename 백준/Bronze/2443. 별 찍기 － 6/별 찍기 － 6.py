stairs = int(input())
star = 2*stairs-1
blank = 1
for stair_count in range(0,stairs):
    for blank_count in range(1,blank):
        print(" ",end="")
    blank +=1
    for star_count in range(star,0,-1):
        print("*",end="")
    star -=2
    print()