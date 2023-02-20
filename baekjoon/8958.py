t = int(input())

for _ in range(t):
  array = list(input())
  pre = array[0]
  cnt = 0
  total = 0
  if pre == 'X':
    cnt = 0
  else:
    cnt = 1
    total += 1
  for i in range(1, len(array)):
    if array[i] == 'O' and pre == array[i]:
      cnt += 1
      total += cnt
    elif array[i] == 'O' and pre != array[i]:
      cnt = 1
      total += cnt
    pre = array[i]

  print(total)
      