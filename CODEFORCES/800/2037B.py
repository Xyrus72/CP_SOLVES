t=int(input())
for _ in range (t):
    a=int(input())
    b=list(map(int,input().split()))
    baki=a-2
    #b.sort()
    arr=[]
    for i in range (1,baki+1):
        if baki%i==0:
            arr.append(i)
    #print(arr)
    c=0    
    for m in range(len(arr)):
        x=arr[m]
        rest=int(baki/x)
        c=0
        
        if x in b:
            c+=1
            
        if rest in b:
            c+=1
            if c==2:
                print(x,'',rest)
                break
        
            
            
        
    
    
    
    
    
   
        