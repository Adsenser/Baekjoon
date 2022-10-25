a = int(input())
for i in range(a):
    b = input()
    sum = 0
    result = 0
    for j in range(len(b)):
        if b[j] == 'O':
            sum += 1
            result += sum
        else:
            sum = 0

    print(result)