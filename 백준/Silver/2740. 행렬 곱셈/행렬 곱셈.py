n, m = map(int,input().split())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

m, k = map(int,input().split())
B = []
for i in range(m):
    B.append(list(map(int,input().split())))
result = []
temp_list = []
for i in range(n):
    for j in range(k):
        line_sum = 0
        for t in range(m):
            line_sum += A[i][t] * B[t][j]
        temp_list.append(line_sum)
    result.append(temp_list)
    temp_list = []
for i in range(n):
    for j in range(k):
        print(result[i][j],end=" ")
    print()