line1 = list(input())
line2 = list(input())
line3 = list(input())
line4 = list(input())
line5 = list(input())
line6 = list(input())
line7 = list(input())
line8 = list(input())

line1.extend(line3)
line1.extend(line5)
line1.extend(line7)

result = 0
for j in range(0,32,2):
    if line1[j] == 'F':
        result +=1

line2.extend(line4)
line2.extend(line6)
line2.extend(line8)

for j in range(1,33,2):
    if line2[j] == 'F':
        result +=1

print(result)