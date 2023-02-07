s = list(input())

sum = 0
array = []

for i in s:
  if i<'9' and i>'0':
    sum += int(i)
  else:
    array.append(i)

array.sort()

for i in array:
  print(i, end='')

if sum !=0:
  print(sum)
  