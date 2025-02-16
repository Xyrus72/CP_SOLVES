import math
l=list(map(int,input().split()))
arr=[0]*1001
for i in range(2,1001):
    if arr[i]==0:
        for k in range(i*i,1001,i):
            arr[k]=1
#print(arr)
primes = [i for i in range(2, l[0] + 1) if arr[i] == 0]
#print(primes)
c=0
old=primes[0]
new=0
for j in range (1,len(primes)):
    new=primes[j]
    if old + new + 1 >l[0]:
        break
    if arr[old+new+1]==0 and old + new + 1 <=l[0]:
        c+=1
        old=new
    else:
        old=new
            
if l[1]<=c:
    print('YES')
else:
    print('NO')
    
#print(c)