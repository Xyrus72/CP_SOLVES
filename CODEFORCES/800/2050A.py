t=int(input())
for _ in range (t):
    n,m=map(int,input().split())
    c=0
    key=0
    for __ in range(n):
        s=input()
        l=len(s)
        if l<=m and key==0:
            m-=l
            c+=1
        else:
            key=1
            #print(0)
            continue
    if c==0:
        print(0)
    else:
        print(c)
        
        
    