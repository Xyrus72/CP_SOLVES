t=int(input())
for _ in range (t):
    l=int(input())
    arr=list(map(int,input().split()))
    left=l//2
    right=left-1
    
    c1=0
    c2=l-1
    while c1<left or c2>right:
        if c1<left:
            print(arr[c1],end=' ')
            c1+=1
        if c2>right:
            print(arr[c2],end=' ')
            c2-=1
            
    print()