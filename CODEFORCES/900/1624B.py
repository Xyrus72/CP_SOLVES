v=int(input())
for i in range (v):
    a,b,c=map(int,input().split())
    count=0
    
    if (2*b-c)%a==0 and (2*b-c)>0:
        
        print("YES")
        count+=1
    elif (2*b-a)%c==0 and (2*b-a)>0:
        
        print("YES")
        count+=1
    elif ((a+c))%(2*b)==0:
        print("YES")
        count+=1
    else:
        print("NO")
        
        