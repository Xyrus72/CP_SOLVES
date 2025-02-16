t=int(input())
for _ in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    x=sum(a)
    even=0
    odd=0
    if x%n==0:
        if n%2==1:
            even_num=(n//2 )+1
        else:
            even_num=(n//2 )
            
        even_sum=(x/n)*even_num
        #print(even_sum)
        s=0
        for i in range (n):
            if i%2==0:
                s+=a[i]
        #print(s)
        if s==even_sum:
            print('yes')
        else:
            print('no')
                
        
        
        
    else:
        print('no')
    