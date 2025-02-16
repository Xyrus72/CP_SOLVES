t=int(input())
for _ in range (t):
    n=int(input())
    arr=[0]*n
    for i in range (1,n+1):
        arr[i-1]=i
    #print(arr)
    last=arr[n-1]
    for j in range(n-1,0,-1):
        arr[j]=arr[j-1]
    #print(arr)
    arr[0]=last
    print(" ".join(map(str, arr)))
        
    
    