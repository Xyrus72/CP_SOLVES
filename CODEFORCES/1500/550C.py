a = input()
idx = 0
c = 0
x = a.split()
zero = [0, 4, 8, 12, 16, 20]  # only 0 thakleo ans 
two = [3, 7, 11, 15, 19]
four = [2, 6, 10]
six = [1, 5, 9]
eight = [0, 4, 8, 12]  # only 8 thakleo ans
efficient=[] # this gonna stiore the val that has been already checked so that it doesnt repeat the loops again
 
for i in range(len(a) - 1, -1, -1):
    if c==1:
        break
    a=a[:i+1:]
    if a[i] == '0':
        c += 1
        print('yes')
        print(0)
        break
    elif a[i] == '8':
        c += 1
        print('yes')
        print(8)
        break
    elif a[i] == '2':
        for k in range(i - 1, -1, -1):
            if c==1:
                break
            if a[k] == '3' or a[k] == '7':
                if a[k]=='3':
                    store='3'
                    print('yes')
                    print(int(store + '2'))
                    c += 1
                    break
                else:
                    store='7'
                    
                    print('yes')
                    print(int(store + '2'))
                    c += 1
                    break
                
                
            elif a[k] == '1' or a[k] == '5' or a[k]=='9':
                if a[k]=='1':
                    store='1'
                elif a[k]=='9':
                    store='9'
                else:
                    store='5'
                idx = k
                for k1 in range(idx - 1, -1, -1):
                    if int(a[k1]) % 2 == 1:
                        if idx==0:
                            print('yes')
                            print(int(a[k1] + '2'))
                            c += 1
                            break
                        else:
                            
                            print('yes')
                            print(int(a[k1] +store+ '2'))
                            c += 1
                            break
    elif a[i] == '4':
        if c==1:
            break
        for k in range(i - 1, -1, -1):
            if c==1:
                break
            if a[k] == '2' or a[k] == '6':
                if a[k]=='2':
                    store='2'
                    print('yes')
                    print(int(store + '4'))
                    c += 1
                    break
                else:
                    store='6'
                    print('yes')
                    print(int(store+ '4'))
                    c += 1
                    break
                
                        
            elif a[k] == '4' or a[k] == '8':
                if a[k]=='4':
                    store='4'
                else:
                    store='8'
                idx = k
                for k1 in range(idx , -1, -1):
                    if int(a[k1]) % 2 == 1:
                        if idx==0:
                            print('yes')
                            print(int(a[k1] + '4'))
                            c += 1
                            break
                        else:
                            
                            print('yes')
                            print(int(a[k1] +store+ '4'))
                            c += 1
                            break
    elif a[i] == '6':
        
        for k in range(i - 1, -1, -1):
            if c==1:
                break
            if a[k] == '1' or a[k] == '5' or a[k] == '9':
                if a[k]=='1':
                    store='1'
                    print('yes')
                    print(int(store + '6'))
                    c += 1
                    break
                elif a[k]=='5':
                    store='5'
                    print('yes')
                    print(int(store + '6'))
                    c += 1
                    break
                else:
                    store='9'
                    print('yes')
                    print(int(store + '6'))
                    c += 1
                    break
                
            elif a[k] == '3' or a[k] == '7':
                if a[k]=='3':
                    store='3'
                else:
                    store='7'
                idx = k
                for k1 in range(idx - 1, -1, -1):
                    if int(a[k1]) % 2 == 1:
                        if idx==0:
                            print('yes')
                            print(int(a[k1] + '6'))
                            c += 1
                            break
                        else:
                            
                            print('yes')
                            print(int(a[k1] +store+ '6'))
                            c += 1
                            break
 
if c == 0:
    print('no')