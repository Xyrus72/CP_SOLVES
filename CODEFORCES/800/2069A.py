n=int(input())
for _ in range (n):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    key=0
    if a==3:
        print('YES')
        continue
    start=0    
    for i in range (len(b)-2):
        if b[0]==0 and start==0:
            start=1
            continue
        elif b[i]==1:
            if b[i+1]==0:
                if b[i+2]==1:
                    print('NO')
                    key=1
                    break
    if key==0:
        print('YES')
        