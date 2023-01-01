import sys
n = int(input())
for _ in range(n): # 테스트 케이스1
    m = int(input())
    line = []
    for _ in range(m): # 1번 라인
        b = sys.stdin.readline().rstrip().split()[1]
        line.append(b)
        # print(line)
    line.sort() # 개수 판단 알고리즘 시작
    # print(line)
    index = 1
    count_index = [1]
    for i in range(m-1):
        if line[i] == line[i+1]:
            count_index[-1] += 1
        else:
            count_index.append(index)
    # print(count_index)
    if len(count_index) >= 2:
        result = 1
        for i in count_index:
            result *= i+1
        print(result-1)
    else:
        print(m)