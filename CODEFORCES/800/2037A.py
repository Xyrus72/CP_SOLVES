t=int(input())
for _ in range (t):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(a):
        #key=0
        if b[i]==0:
            continue
        for j in range (i+1,a):
            if b[j]==0:
                continue
            if b[i]==b[j]:
                #key=1
                c+=1
                b[j]=0
                b[i]=0
        
            
    print(c)
                