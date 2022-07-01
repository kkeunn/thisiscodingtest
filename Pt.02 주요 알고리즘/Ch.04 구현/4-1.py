import sys

n = int(sys.stdin.readline())

x, y = 1, 1
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
direction = {"L":1, "R":0, "U":3, "D":2}

data = tuple(map(str, sys.stdin.readline().split()))

for d in data:
    nx = x + dx[direction[d]]
    ny = y + dy[direction[d]]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x, y = nx, ny
    
print(x, y)