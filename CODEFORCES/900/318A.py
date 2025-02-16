k,n=map(int,input().split())
div1=k/2
div2=k//2
if div1>div2:
    mid=div2+1
    #print(mid)
    if n<=mid:
        print((n*2)-1)
    else:
        n=n-mid
        #print(n)
        print(n*2)
else:
    mid=div2
    if n<=mid:
        print((n*2)-1)
    else:
        n=n-mid
        print(n*2)
        