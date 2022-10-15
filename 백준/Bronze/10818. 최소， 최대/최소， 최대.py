number = int(input())
numbers = list(map(int,input().split(" ")))
a = int(min(numbers))
b = int(max(numbers))

print("%d %d" % (a,b))