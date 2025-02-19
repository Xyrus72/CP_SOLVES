n=int(input())
#n=1
for _ in range (n):
    shelves,bottle=map(int,input().split())
    arr=[0]*(bottle+1)
    for __ in range (bottle):
        idd,num=list(map(int,input().split()))
        
        arr[idd]+=num
    arr.sort(reverse=True)
    c=0
    for i in range(shelves):
        
        c+=arr[i]
        if i+1>len(arr)-1:
            break
    print(c)
        