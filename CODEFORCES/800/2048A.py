t=int(input())
for _ in range (t):
    x=input()
    i=0
    key=0
    if int(x)<33:
        print('no')
        continue
    while  int(x)>32 :
        x=str(x)
        i=0
        if int(x)==33:
            print('yes')
            key=1
            break
        elif int(x)<33:
            print('no')
            key=1
            break
            
        while i<(len(x)-1):
            if len(x)==0:
                print('no')
                key=1
                break
                
            if x[i]=='3' and x[i+1]=='3':
                x=x[:i]+x[i+2::]
                i-=1
            i+=1
            
        if len(x)!=0:    
            x=int(x)
           
                
            if 0<int(x)<33:
                print('no')
                key=1
                break
            elif int(x)==0:
                print('yes')
                key=1
                break
                
            else:
                x-=33
        else:
            print('yes')
            key=1
            break
            
            
    #print(x)
    if x==0:
        if key==0:
            print('yes')
    else:
        if key==0:
            print('no')
            
          