t=int(input())
#t=1
for _ in range (t): 
    k,n=map(int,input().split())
    s=input()
    c=0
    old=0
    pre=[0]*(k+1)
    total=0
    
        
    for i in s:
        c+=1
        if i=="W":
            total+=1
            pre[c]+=total
        else:
            pre[c]=total
        
    #print(pre)
    mini=999999
    #n=n-1
    
    if k==1 and n==1:
        if s[0]=="W":
            print(1)
        else:
            print(0)
        continue
    if k==n:
        print(pre[k])
        continue
        
        
    
    if max(pre)==k:
        print(n)
        continue
    for j in range (0,(k)-(n-1)):
        #print(j)
        diff=pre[j+(n)]-pre[j]
        if diff <mini:
            mini=diff
    print(mini)
        
    
    
    