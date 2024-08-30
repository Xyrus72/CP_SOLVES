a = int(input())
for i in range(a):
    maxx, choose, sum_required = map(int, input().split())
    low = maxx - choose + 1
    s1 = (choose / 2) * (low + maxx)
    s2=(choose / 2) * (choose+1)
    
    if s1 >= sum_required and s2<=sum_required:
    
        print('yes')
    else:
        print('no')

