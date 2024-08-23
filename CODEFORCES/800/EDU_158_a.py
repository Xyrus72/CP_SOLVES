a=int(input())
for i in range (a):
    m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    max1=0
    for k in range(len(l)-1):
        if abs(l[k]-l[k+1])>max1:
            max1=abs(l[k]-l[k+1])
    max2=abs(m[len(m)-1]-l[len(l)-1])
    max2*=2
    if max1>max2:
        print(max1)
    else:
        print(max2)
    
        