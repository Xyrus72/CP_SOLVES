a=int(input())
for i in range (a):
    b=int(input())
    c=list(map(int,input().split()))
    plus=0
    minus=0
    for j in  (c):
        if j>0:
            plus+=j
        else:
            minus+=j
    print(plus-minus)
        