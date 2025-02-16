x,y= map(int, input().split())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
#print(arr)
pre=[0]*(x+1)
total=0
for i in range (0,len(arr)):
    total+=arr[i]
    pre[i+1]=total
#print(pre)
for z in range (y):
    a,b= map(int, input().split())
    o=a-b
    print(pre[a]-pre[o])