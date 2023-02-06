n = int(input())
array=[0]*n

for i in range(n):
  array[i] = int(input())

  '''
  array=[]
  for i in range(n):
    array.append(int(input()))
  '''

array.sort(reverse=True)
for i in range(len(array)):
  print(array[i], end=' ')

'''
for i in array:
  print(i, end=' ')
'''