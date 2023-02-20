from itertools import product

n, m = map(int, input().split())

array = [i for i in range(1, n+1)]

lists = list(product(array, repeat=m))

for data in lists:
  data = list(data)
  for i in data:
    print(i, end=' ')
  print()