import math
n=int(input())
 
for _ in range (n):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    m=b[0]
    h=1
    for i in range(1,len(b)):
        if b[i]<=m:
            prev=m
            calc= math.ceil(m/b[i])
            if calc*b[i]<=m:
                calc+=1
                m=calc*b[i]
            else:
                m=calc*b[i]
        else:
            m=b[i]
    print(m)