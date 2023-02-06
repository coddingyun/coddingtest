n = int(input())

array=[]

for i in range(n):
  #input_data = input().split()
  #array.append((input_data[0], int(input_data[1])))
  array.append(list(map(str, input().split())))
  
def func(array):
  return int(array[1])
result=sorted(array, key=func)

for i in result:
  print(i[0], end=' ')