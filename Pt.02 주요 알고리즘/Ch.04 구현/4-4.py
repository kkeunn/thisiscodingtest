import sys
n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
news = (0, 1, 2, 3)

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

d = news[d-1]
array = []
for _ in range(m):
    array.append(list(map(int, sys.stdin.readline().split())))
    
cnt = 1
rotation = 0  
while 1:
    d = news[d-1]
    nx = x + dx[d]
    ny = y + dy[d]
    if array[nx][ny]== 1 or array[nx][ny] == 2:
        rotation += 1
        if rotation == 4:
            nx = x-dx[d]
            ny = y-dx[d]
            if array[nx][ny] == 2:
                x, y = nx, ny
            break
        else:
            continue
    array[nx][ny] = 2
    cnt += 1
    x, y = nx, ny

print(cnt)