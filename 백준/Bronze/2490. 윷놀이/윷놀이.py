a1,a2,a3,a4 = map(int,input().split(" "))
b1,b2,b3,b4 = map(int,input().split(" "))
c1,c2,c3,c4 = map(int,input().split(" "))

A = a1+a2+a3+a4
B = b1+b2+b3+b4
C = c1+c2+c3+c4

if A==4:
    print("E")
elif A==3:
    print("A")
elif A==2:
    print("B")
elif A==1:
    print("C")
else:
    print("D")
    
if B==4:
    print("E")
elif B==3:
    print("A")
elif B==2:
    print("B")
elif B==1:
    print("C")
else:
    print("D")
    
if C==4:
    print("E")
elif C==3:
    print("A")
elif C==2:
    print("B")
elif C==1:
    print("C")
else:
    print("D")