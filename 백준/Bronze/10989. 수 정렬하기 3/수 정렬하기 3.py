import sys
input = sys.stdin.readline

a = int(input())
b =[0]*10001

for _ in range(a):
    temp = int(input())
    b[temp] += 1 #미리 배열 만들어 놓고 입력된 숫자 위치에 1씩 카운트

for i in range(10001): #어차피 오름차순으로 출력되므로 문제에서 제시한 것 처럼 나오게 됨
    if b[i] != 0: # 중복된 숫자가 있을 수 있으므로 1씩 카운트 된것 만큼 반복시켜줘야 함
        for j in range(b[i]): #카운트 된 것 만큼 반복
            print(i) #그 위치의 인덱스 번호가 출력됨
