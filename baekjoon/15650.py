from itertools import combinations

n, m = map(int, input().split())

array = [i for i in range(1, n+1)]

lists = list(combinations(array, m))

for data in lists:
  data = list(data)
  data.sort()
  for i in data:
    print(i, end=' ')
  print()