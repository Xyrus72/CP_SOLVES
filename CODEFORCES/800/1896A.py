a=int(input())
for i in range (a):
    m=int(input())
    l=list(map(int,input().split()))
    x=l.copy()
    x.sort()
    
    for k in range (m):
        for j in range (1,m-1):
            if l[j-1]<l[j] and l[j]>l[j+1]:
                c=l[j]
                l[j]=l[j+1]
                l[j+1]=c
            #print(l)
    if l==x:
        print('yes')
    else:
        print('no')
        
