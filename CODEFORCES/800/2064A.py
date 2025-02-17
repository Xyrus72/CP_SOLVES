a=int(input())
#a=1
for _ in range (a):
    b=int(input())
    c = input()

    key=0
    count=0
    for i in range (b-1):
        if  c[i]=='0' and c[i+1]=='1':
            count+=1
            
               
        elif c[i]=='1' and c[i+1]=='0':
            count+=1
    if c[0]=='1':
        count+=1
    print(count)
            
                