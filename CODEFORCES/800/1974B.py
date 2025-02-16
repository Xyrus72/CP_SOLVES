import math
a=int(input())
for _ in range (a):
    d=int(input())
    b=input()
    l=[]
    for j in b:
        l.append(j)
    #print(l)
    diff=set(l)
    #print(diff)
    same_na=list(diff)
    same_na=sorted(same_na)
    #print(same_na)
    adha=len(same_na)//2
    ulta=len(same_na)-1
    #dic={}
    ak=[]
    dui=[]
    #print(same_na)
    for i in range (adha):
        shamne=same_na[i]
        piche=same_na[ulta-i]
        ak.append(shamne)
        dui.append(piche)
        #print(ak)
        #print(dui)
    
    
    
    for i in b:
        key=0
        for k in range(len(ak)):
            if i==ak[k]:
                print(dui[k],end='')
                key=1
                break
            elif i==dui[k]:
                print(ak[k],end='')
                key=1
                break
        if key==0:
            print(i,end='')
    print()
        