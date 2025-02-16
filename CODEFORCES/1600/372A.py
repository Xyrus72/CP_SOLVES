a=int(input())
#a=1
arr=[]
for _ in range(a):
    n=int(input())
    arr.append(n)
arr.sort()
#print(arr)
mid=a//2

choto=0
boro=mid
count=0
while choto<mid and boro<a:
    c=arr[choto]
    b=arr[boro]
    checker=b//2
    if checker>=c:
        count+=1
        choto+=1
        boro+=1
    elif checker<c:
        boro+=1
visible=a-int(count*2)
print(int(visible+count))
    