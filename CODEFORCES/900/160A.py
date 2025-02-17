import math
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)

mid = math.ceil(n / 2)
key=0
for i in range (1,n):
    f1=l[:i]
    f2=l[i:]
    if sum(f1)>sum(f2):
        print(i)
        key=1
        break
    
if key==0 and n==1:
    print(1)
elif key==0:
    print(n)