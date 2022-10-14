number = int(input())
while True:
    for j in range(2,number+1):
        if number%j == 0:
            number = number//j
            print(j)
            break
    if number == 1:
        break