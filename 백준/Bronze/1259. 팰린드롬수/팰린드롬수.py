while True:

    a = list(input())
    if a == ['0']:
        break
    else:
        aa = reversed(a)
        aa = list(aa)
        if a == aa:
            print("yes")
        else:
            print("no")
