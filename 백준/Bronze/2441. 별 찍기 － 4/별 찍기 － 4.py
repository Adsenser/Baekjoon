line = int(input())
blank_plus = 0
for line_count in range(1,line+1):
    for blank in range(0,blank_plus):
        print(" ",end="")
    blank_plus +=1
    for star in range(line_count,line+1,1):
        print("*",end="")
    print()