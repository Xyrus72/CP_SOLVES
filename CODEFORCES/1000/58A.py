a=input()
s='hello'
c=0
total=0
for i in range (len(a)):
    if a[i]==s[c]:
        c+=1
        if c==5:
            print('YES')
            break
if c!=5:
    print('NO')

    
    
        
        
