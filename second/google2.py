for _ in range(int(input())):
  n = int(input())
  arr1 = list(map(int, input().split()))
  m = int(input())
  arr2 = list(map(int, input().split()))
  max = 0
  max_num = 1
  min = int(1e9)
  min_num = 1
  for i in range(n):
    if arr1[i]>max:
      max = arr1[i]
    if arr1[i]<min:
      min = arr1[i]

  for i in range(n):
    if arr2[i]>max:
      max = arr2[i]
      max_num = 2
    if arr2[i]<min:
      min = arr2[i]
      min_num = 2

  first = []
  if max_num == 1:
    for i in range(n):
      first.append(arr1[i])
      if arr1[i] == max:
        break
    if min_num == 2:
      for j in range(m):
        first.append(arr2[j])
        if arr2[j] == min:
          break
  else:
    for i in range(m):
      first.append(arr2[i])
      if arr2[i] == max:
        break
    if min_num == 1:
      for j in range(m):
        first.append(arr1[j])
        if arr1[j] == min:
          break

  second = []
  if min_num == 1:
    for i in range(n):
      second.append(arr1[i])
      if arr1[i] == min:
        break
    if max_num == 2:
      for j in range(m):
        second.append(arr2[j])
        if arr2[j] == max:
          break
    
  
      
  