a = int(input())
b = []
for i in range(a):
    enter = list(input())
    b.append(enter)
result = ''
t = 0
o = 1 # 열 값 같은지 확인
for j in range(len(enter)):
    while t < a-1:
        if b[t][j] == b[t+1][j]:
            o = 1
        else:
            o = 0
        t += 1
    if o == 1:
        result += enter[j]
    if o == 0:
        result += '?'
    o = 0
    t = 0
    if a ==1:
        o = 1
print(result)
