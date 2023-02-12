g = int(input())
p = int(input())

array = []

for i in range(p):
  array.append(int(input()))

gates = [False] * g

count = 0
for i in range(p):
  index = array[i]
  r = False
  for j in range(index-1, -1, -1):
    if gates[j] == False:
      gates[j] = True
      count += 1
      r = True
      break
  if r == False:
    break

print(count)