a = int(input())
n = 2
u = 1


while True:
    if a == 1:
        print(1)
        break
    if n <= a < n +(6*(u)):
        print(u+1)
        break
    else:
        n += (6 * u)
        u +=1