a=int(input())
for i in range (a):
    m=int(input())
    l=input()
    x=[0]
    count=0
    h=0
    key=0
    for i in l:
        if i=='.':
            count+=1
        else:
            x.append(count)
            count=0
   
    x.append(count)
        
    #print(x)
    h=max(x)
    if h>2:
        print(2)
    else:
        print(sum(x))
    
