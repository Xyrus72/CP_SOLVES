a=int(input())
for _ in range (a):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    
    x1=set(x)
    x2=set(y)
    q1=len(x1)
    q2=len(x2)
    if q1==1 and q2>2:
        print('yes')
    elif q2==1 and q1>2:
        print('yes')
    elif q1>1 and q2>1:
        print('yes')
    else:
        print('no')