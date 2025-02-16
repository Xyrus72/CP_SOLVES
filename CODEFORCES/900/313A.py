a=input()
if int(a)>0:
    print(a)
else:
    if int(a[-2])>int(a[-1]):
        x=a[-1]
        s=a[:len(a)-2:]
        s+=x
        print(int(s))
    else:
        x=a[-2]
        s=a[:len(a)-2:]
        s+=x
        print(int(s))