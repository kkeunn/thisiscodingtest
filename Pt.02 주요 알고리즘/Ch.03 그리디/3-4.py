import sys
n, k  = map(int, sys.stdin.readline().split())

cnt = 0
while 1:
    if n%k == 0:
        n /= k
    else:
        n -= 1
    cnt += 1
    
    if n == 1:
        break

print(cnt)