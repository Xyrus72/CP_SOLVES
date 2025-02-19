a=input()
c=0
f1=0
f2=0
for i in a:
    if i=='4' or i=='7':
        c+=1
if c==len(a):
    print('YES')
else:
    if int(a)%4==0 or int(a)%7==0 or int(a)%47==0 or int(a)%477==0 or int(a)%74==0 or int(a)%747==0 or int(a)%474==0 or int(a)%777==0 :
        print('YES')
    else:
        print('NO')
        
        