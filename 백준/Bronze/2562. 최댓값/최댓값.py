number = []
for i in range(9):
    number.append(int(input()))
for n in range(1,10):
    if number[n-1] == max(number):
        max_count = n
        max_number = number[n-1]
print("%d\n%d" % (max_number,max_count))
