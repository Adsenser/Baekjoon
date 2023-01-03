import sys
n, m = map(int,input().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
sum = 0
prefixed_sum =[0]
for i in range(n):
    sum += arr[i]
    prefixed_sum.append(sum)
for k in range(m):
    i, j = map(int,sys.stdin.readline().rstrip().split())
    print(prefixed_sum[j]-prefixed_sum[i-1])