a=int(input())
for i in range (a):
    m=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    #print(s)
    com=[]
    count=0
    even=[]
    if m<3:
        print('yes')
        continue
    
    for j in s:
        count=0
        for i in range (len(l)):
            if l[i]==j:
                count+=1
        if count%2==0:
            even.append(0)
        com.append(count)
    #print(com)
    #print(even)
    if len(com)<3:
        if len(com)==2:
            if abs(com[0]-com[1])==1:
                print('yes')
            elif  len(even)==len(com):
                print('yes')
            else:
                print('no')
            
        else:
           print('yes')
    
    
    
    else:
        print('no')
        
                
