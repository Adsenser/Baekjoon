import sys
while True:
    a = sys.stdin.readline().rstrip()
    if a == '.':
        break
    b = []
    ok = True
    for i in range(len(a)):
        if a[i] == '(' or a[i] == '[':
            b.append(a[i])
        elif a[i] == ')':
            if len(b) >= 1:
                if b[-1] == '(':
                    b.pop()
                else:
                    ok = False
                    break
            else:
                ok = False
                break
        elif a[i] == ']':
            if len(b) >= 1:
                if b[-1] == '[':
                    b.pop()
                else:
                    ok = False
                    break
            else:
                ok = False
                break

    if len(b) == 0 and ok==True:
        print("yes")
    else:
        print("no")
