import sys
input = sys.stdin.readline

count = 0
n = int(input().rstrip())

for _ in range(n):
    arr = []
    keyword = input().rstrip()
    for i in range(len(keyword)):
        if arr:
            if arr[-1] == keyword[i]:
                arr.pop()
            else:
                arr.append(keyword[i])
        else:
            arr.append(keyword[i])
    if len(arr)==0:
        count += 1
print(count)