import sys
box = set()
for i in range(int(input())):
    box.add(sys.stdin.readline().rstrip())
box = list(box)
box.sort()
box.sort(key=lambda x:len(x))
for j in box:
  print(j)