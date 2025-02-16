n=int(input())
for _ in range (n):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range (a-1):
        add=b[i+1]-b[i]
        if add<0:
            add=add*(-1)
        
        if add==5 or add==7:
            c+=1
    if c==a-1:
        print('yes')
    else:
        print('no')
            
            
        
    