import sys
a = []
for _ in range(91):
    a.append(0)
check = str(sys.stdin.readline().rstrip())
check = check.upper()
for i in check:
    a[ord(i)] += 1
max_num = 0; overlap_count=0; max_num = 0
for j in range(65,91,1):
    if a[j] > max_num:
        max_num = a[j]
        max_index = j
        overlap_count += 1
    elif overlap_count >= 1 and a[j]==max_num:
        max_index = 63
print(chr(max_index))
