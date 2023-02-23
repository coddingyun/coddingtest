n = int(input())

array = []

for _ in range(n):
  array.append(list(input().split()))

array.sort(key = lambda x: [-int(x[1]), int(x[2]), -int(x[3]), x[0]])

for data in array:
  name, kor, eng, math = data
  print(name)