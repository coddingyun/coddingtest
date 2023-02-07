s = list(map(int, input()))

pre = s[0]

num_0 = 0
num_1 = 0

if pre == 0:
  num_0+=1
else:
  num_1+=1

for i in s[1:]:
  if pre == i:
    continue
  else:
    if i == 0:
      num_0+=1
    else:
      num_1+=1
  pre = i

print(min(num_0, num_1))