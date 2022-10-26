a = int(input())
for i in range(a):
    b,c = input().split(" ")
    for j in range(len(c)):
        for k in range(int(b)):
            print(c[j],end="")
    print()