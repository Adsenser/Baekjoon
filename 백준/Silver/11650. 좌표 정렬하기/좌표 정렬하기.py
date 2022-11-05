arr = [list(map(int, input().split())) for i in range(int(input()))]
arr.sort()

for q,w in arr:
    print(q,w)