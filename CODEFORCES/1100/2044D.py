a=int(input())
for _ in range (a):
    n=int(input())
    arr=list(map(int,input().split()))
    new=[0]*(n+1)
    
    x=[]
    
    for i in range (n):
        if new[arr[i]]==1:
            continue
        else:
            print(arr[i],end=' ')
            new[arr[i]]=1
            
    #print(new)
            
   
    for k in range(1,len(new)):
        if new[k]!=1:
            print(k,end=' ')
        
        
    
            
    print()
        
    
            
            
    
    