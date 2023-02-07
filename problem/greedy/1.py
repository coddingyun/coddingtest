n = int(input())

array = list(map(int, input().split()))

array.sort()

number = 0
i=0
while i<n:
  cond = True
  for j in range(i,i+array[i]):
    if j>=n or array[j]>array[i]:
      cond = False
      break
  if cond == True:
    number+=1
    i=i+array[i]
  else:
    break

print(number)
