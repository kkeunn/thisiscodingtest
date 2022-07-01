import sys
n, m = map(int, sys.stdin.readline().split())

result = 0
for _ in range(n):
   cards = map(int, sys.stdin.readline().split())
   result = max(result,min(cards))
   
print(result)