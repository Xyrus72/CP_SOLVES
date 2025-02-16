a=input()
arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U','y','Y']
for i in range (len(a)):
    if a[i] in arr:
        continue
    elif ord(a[i])<97:
        print('.',end='')
        print (chr(ord(a[i])+32),end='')
    elif ord(a[i])>96:
        print('.',end='')
        print (a[i],end='')
    

            
        
    
    
    