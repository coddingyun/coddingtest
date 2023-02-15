for _ in range(int(input())):
  n = int(input())
  value = n // 10
  array = []
  while value>=0:
    partial_array = list(map(int, input().split()))
    for i in partial_array:
      array.append(i)
    value-=1
  result = []
  array2 = []
  for i in range(n):
    array2.append(array[i])
    if i%2 == 0:
      array2.sort()
      result.append(array2[i//2])
  print(len(result))
  for i in range(len(result)):
    if i%10==0 and i!=0:
      print()
    print(result[i], end=' ')
  print()