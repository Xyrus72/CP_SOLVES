a = int(input())
for _ in range(a):
    b = list(map(int, input().split()))
    y = set(b)
    
    if len(y) < 2:
        a3 = 0
    else:
        a3 = b[0] + b[1]
    
    b.insert(2, a3)
    count = 0
    
    for i in range(len(b) - 2):
        if b[i] + b[i + 1] == b[i + 2]:
            count += 1
    
    #print(count)
    count2=0
    if count==1 or count==2:
        x=b[3]-b[1]
        b[2]=x
        for i in range(len(b) - 2):
            if b[i] + b[i + 1] == b[i + 2]:
                count2 += 1
    print(max(count,count2))
        
        
        
        
        
        
        
        
        
        