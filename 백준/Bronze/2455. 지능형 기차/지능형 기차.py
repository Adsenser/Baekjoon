people = []
for i in range(4):
    people.append(map(int,input().split(" ")))
peoples = []
for j in people:
    peoples.extend(j)

count = []
sum = 0
for n in range(1,9):
    if n%2 != 0:
        sum = sum - peoples[n-1]
    else:
        sum += peoples[n-1]
    count.append(sum)
print(max(count))