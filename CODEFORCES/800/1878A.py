_=int(input())
for i in range (_):
    
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    if a[1] in b:
        print("YES")
    else:
        print("NO")