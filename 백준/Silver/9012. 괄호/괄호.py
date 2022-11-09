import sys
k = int(input())
for _ in range(k):
    T = True
    a = sys.stdin.readline().rstrip()
    b = []
    for i in range(len(a)):
        if a[i] == '(':
            b.append(a[i])
        elif a[i] == ')':
            if len(b) >= 1:
                if b[-1] == '(':
                    b.pop()
            else:
                T = False
                break
    if len(b) == 0 and T == True:
        print("YES")
    elif len(b) != 0 or T == False:
        print("NO")
