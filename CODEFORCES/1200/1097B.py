n = int(input())
a=[]
for l in range (n):
    t=int(input())
    a.append(t)
#print(1 << n)    
p = False
for i in range(1 << n):  
    total_sum = 0
    for j in range(n):
        if i & (1 << j):  
            total_sum += a[j]
        else:  
            total_sum -= a[j]
        
    total_sum %= 360
    if total_sum == 0:
        p = True
        break

if p:
    print("YES")
else:
    print("NO")