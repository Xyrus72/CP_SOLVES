a=int(input())
for i in range (a):
    b=list(map(int,input().split()))
    m=0
    
    for  x in range(len(b)):
        if b[x]==0:
            print(0)
            break
        else:
            if b[x]<0:
                b[x]=abs(b[x])
    b.sort()
    print(b[0])