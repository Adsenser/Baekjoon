import sys
l = int(input())
block = map(int,sys.stdin.readline().rstrip().split())
block = list(block)
block.sort()
n = int(input())
etc = 0

for i in range(len(block)-1):
    if block[i] < n and block[i+1] > n:
        start = block[i]
        end = block[i+1]
    elif n < block[0]:
        start = 1
        end = block[0]
        etc = 1
        break
if etc == 0:
    try:
        first = (n - (start+1)) * ((end-1) - n +1 )
        second = end -1 - n
        print(first + second)
    except:
        print("0")
else:
    first = (n - start) * (end - n)
    second = end - 1 -n
    print(first + second)