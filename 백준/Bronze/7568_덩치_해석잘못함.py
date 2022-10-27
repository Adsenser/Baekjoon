a = int(input())
b =[]
c =[]
#2차원 배열로 출력
for i in range(a):
    b = list(map(int,input().split(" ")))
    c.append(b)
#몸무게 파트만 리스트화
d =[]

for j in range(a):
    d.append(c[j][0])
#몸무게 큰 순위로 정렬
dd = d[:]
dd.sort(reverse=True)
#print(dd)
#몸무게에 순위 매기기
e =[] #순위 들어가지는 리스트
r = 1

for k in range(a-1):
    if dd[k] != dd[k+1] :
        e.append(r)
        r +=1
    else:
        e.append(r)
e.append(r)
#몸무게 리스트에 순위 넣어주기

for v in range(a):
    d[v] = e[dd.index(d[v])]

#print(d)

#키 파트만 리스트화
d2 =[]

for j2 in range(a):
    d2.append(c[j2][1])
#몸무게 큰 순위로 정렬
dd2 = d2[:]
dd2.sort(reverse=True)
#print(dd2)
#몸무게에 순위 매기기
e2 =[] #순위 들어가지는 리스트
r2 = 1

for k2 in range(a-1):
    if dd2[k2] != dd2[k+1] :
        e2.append(r2)
        r2 +=1
    else:
        e2.append(r2)
e2.append(r2)
#몸무게 리스트에 순위 넣어주기

for v2 in range(a):
    d2[v2] = e2[dd2.index(d2[v2])]

#print(d2)

## 키와 몸무게 합
d4 = []
for l in range(a):
    d3 = d[l]+d2[l]
    d4.append(d3)

#print(d4)
##최종 순위 도출 파트
d5 =d4[:]
d5.sort()
r3 = 1
r4 = 1
e3 = []
for k3 in range(a-1):
    if d5[k3] != d5[k3+1] :
        e3.append(r3)
        r3 +=1
        r4 +=1
    else:
        e3.append(r3)
        r4 +=1
if d5[-1] == d5[-2]:
    e3.append(r3)
else:
    e3.append(r4)

#print(e3)

## 최종 리스트에 순위 넣어주기

for v3 in range(a):
    d4[v3] = e3[d5.index(d4[v3])]

for nn in range(a):
    print(d4[nn], end=" ")
