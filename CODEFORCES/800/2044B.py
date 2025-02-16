a=int(input())
for i in range (a):
    n=input()
    x=n[::-1]
    #print(x)
    for l in x:
        if l=='q':
            print('p',end='')
        elif l=='p':
            print('q',end='')
        else:
            print('w',end='')
    print()