import sys
from queue import PriorityQueue
raw_list = PriorityQueue()
after_list = []

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    raw_list.put(int(sys.stdin.readline().rstrip()))

if n > 1:

    temp_sum = 0
    temp_sum += raw_list.get()
    temp_sum += raw_list.get()
    after_list.append(temp_sum)
    raw_list.put(temp_sum)

    while True:
        if raw_list.qsize() == 1:
            break
        temp = 0
        temp += raw_list.get()
        temp += raw_list.get()
        after_list.append(temp)
        raw_list.put(temp)

    print(sum(after_list))
else:
    print(0)
