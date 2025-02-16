t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    v = list(map(int, input().split()))

    x = k // 2 + k % 2
    y = k // 2
    cnt = 0
    xd=sum(v)
    high=len(v)
    if xd<=k:
        print(high)
        continue
    i = 0
    while i < n:
        if x - v[i] >= 0:
            x -= v[i]
            cnt += 1
        else:
            #v[i] -= x
            break
        i += 1
    p = i

    i = n - 1
    while i >= p:
        if y - v[i] >= 0:
            y -= v[i]
            cnt += 1
        else:
            #v[i] -= y
            break
        i -= 1

    print(cnt)