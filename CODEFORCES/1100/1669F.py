a=int(input())
#a=1
for _ in range(a):
    n=int(input())
    arr=list(map(int,input().split()))
    mid=(n//2)+1
    left=0
    right=n-1
    l_total=0
    r_total=0
    store=0
    l_total=arr[0]
    r_total=arr[n-1]
    
    
    
    
    if l_total==r_total and n!=1:
        store=2
    elif n==1:
        store=0
    
    while left <=n and right>=0 and (left+1)+(n-right)<=n:
        
        
        #print(l_total)
        #print(r_total)
        #print('sssssssss')
        
        if l_total==r_total:
            store=(left+1)+(n-right  )
            #print(store)
            left+=1
            right-=1
            r_total+=arr[right]
            l_total+=arr[left]
        
        
        elif l_total> r_total:
            right-=1
            r_total+=arr[right]
        else:
            left+=1
            l_total+=arr[left]
    print(store)
