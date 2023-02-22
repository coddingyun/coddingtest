n, m = map(int, input().split())

array = list(map(int, input().split()))

total = 0
for i in range(n):
  for j in range(i+1, n):
    if array[i] != array[j]:
      total += 1

print(total)