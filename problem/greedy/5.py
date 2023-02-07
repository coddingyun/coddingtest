n, m = map(int, input().split())

balls = list(map(int, input().split()))

array = [0] * 11

for ball in balls:
  array[ball] += 1

number = 0

for i in range(1, m+1):
  n-=array[i]
  number += array[i]*n

print(number)