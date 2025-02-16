t=int(input())
#t=1
for _ in range (t):
    n=int(input())
    z=list(map(int,input().split()))
    s=set(z)
    l=list(s)
    ans=0
    
    if n==1:
        print('yes')
        continue
    memory1=z[0]
    memory2=z[n-1]
    for i in z:
        if i==memory1:
            pass
        elif i>memory1:
            ans+=1
            break
        else:
            break
    
    for j in range (n-1,-1,-1):
        if z[j]==memory2:
            continue
        elif z[j]>memory2:
            ans+=1
            break
        else:
            break
        
    old=z[0]   
    for f in range(1,n-1):
        #older hisab rakhte hbe
        if z[f]==z[f+1]:
            pass
        elif z[f]<old and z[f]<z[f+1]:
            ans+=1
            old=z[f]
            
        if z[f+1]!=z[f]:
            old=z[f]
        
    
        
    #print(ans)
    if ans>1:
        print('no')
    else:
        print('yes')