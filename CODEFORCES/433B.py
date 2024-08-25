_=int(input())
a=list(map(int,input().split()))
z=a.copy()
z.sort()
a.insert(0,0)
z.insert(0,0)

b=int(input())
for i in range(1,_+1):
        a[i]=a[i-1]+a[i]
        z[i]=z[i-1]+z[i]
#print(a)
#print(z)
i=0
    


for i in range (b):
    c=list(map(int,input().split()))
    f1=c[1]-1
    f2=c[2]
    if c[0]%2==1:
      
        print(a[f2]-a[f1])
    else:
        print(z[f2]-z[f1])
        
            
