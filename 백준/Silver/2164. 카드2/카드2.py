n = int(input())
arr = []
for i in range(n):
    arr.append(0)
for i in range(n, 0, -1):
    arr.append(i)
j = n - 1
if n != 1:
    while True:
        arr.pop()
        if arr[-2] == 0:
            break
        arr[j] = arr[-1]
        arr.pop()
        j -= 1
    print(arr[-1])
else:
    print(1)