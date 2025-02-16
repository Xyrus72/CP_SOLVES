import math

n = int(input())
a = list(map(int, input().split()))

g = 0
for i in range(n):
    g = math.gcd(g, a[i])

key = 0
if g == 1:
    print(1)
    key = 1

c = 0

for j in range(1, int(math.isqrt(g)) + 1):
    if g % j == 0:
        if j == g // j:  # like for 36 it would count 6x6 twice so gotta have see that tc. then it should count +1. 
            c += 1
        else:  
            c += 2

if key == 0:
    print(c)