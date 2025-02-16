a=int(input())
b=bin(a)
b=b[2::]
#print(b)
c=0
for i in b:
    if i=='1':
        c+=1
print(c)
    
    