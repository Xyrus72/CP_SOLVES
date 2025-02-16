a=int(input())
for _ in range (a):
    b=int(input())
    c=list(map(int,input().split()))
    plus=0
    minus=0
    for i in range(b):
        if i%2==0:
            plus+=c[i]
        else:
            minus+=c[i]
    print((plus-minus))