a = int(input())
for _ in range(a):
    n, m = map(int, input().split())
    x = input()
    s = input()
    
    for i in range(6):
        if s in x:
            print(i)
            break
        x += x
    else:
        print(-1)

