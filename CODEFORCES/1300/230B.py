import math
n=int(input())
l=list(map(int,input().split()))
arr=[0]*10000000
for i in range(2,10000000):
    if arr[i]==0:
        for k in range(i*i,10000000,i):
            arr[k]=1

#print(arr[999983])
#print(arr)
for _ in range (n):
    x=l[_]
    y=math.sqrt(x)
    if x==1:
        print('NO')
    else:
        if x==y*y:
            if y>math.floor(y):
                print('NO')
                
            elif arr[int(y)]==0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    