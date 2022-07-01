import sys
n, m, k = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

first = num_list[-1]
second = num_list[-2]

a = (first*k + second) * (m//(k+1))
b = first*(m%(k+1)) if k >= m%(k+1) else first*k + second*((m%(k+1))-k)

print(a+b)