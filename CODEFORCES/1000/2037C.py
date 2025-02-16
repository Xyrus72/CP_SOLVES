n=int(input())
arr1=[0]*10000000
for i in range(2,10000000):
    if arr1[i]==0:
        for k in range(i*i,10000000,i):
            arr1[k]=1
for _ in range (n):
    a=int(input())
    arr=[]
    for i in range (2,a+1,2):
        if i==4:
            continue
        arr.append(i)
    if a>3:
        arr.append(4)
    if a>4:
        arr.append(5)
    
    for j in range (1,a+1,2):
        if j==5:
            continue
        arr.append(j)
    key=0
    for k in range (a-1):
        if arr1[arr[k]+arr[k+1]]==0:
            print(-1)
            key=1
            break
    if key==0:
        print(*arr)
    
    
        