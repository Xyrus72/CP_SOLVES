t=int(input())
for _ in range (t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    x=arr.copy()
    x.sort()
    if x==arr:
        print('yes')
    elif k==1:
        print('no')
    else:
        print('yes')
    