n, m = map(int,input().split())
cube = []
answer = 1
for _ in range(n):
    temp_line = list(input())
    cube.append(temp_line)
for i in range(1,min(m,n)):#상자 크기 조정
    x = 0
    y = 0
    while True:
        try:
            if int(cube[y][x]) == int(cube[y][x+ i]) == int(cube[y+i][x]) == int(cube[y+ i][x+i]):
                answer = 1+i
                break
            else:
                if x+i+1 == m:
                    y +=1
                    x = 0
                else:
                    x += 1
        except:
            break
print(answer**2)