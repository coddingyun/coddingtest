n = input()
answer = []

if n[0] == '?':
  if n[1] == '?':
    answer.append(2)
  elif int(n[1])>=4:
    answer.append(1)
  else: # 4보다 작거나 ?인 경우
    answer.append(2)
else:
  answer.append(int(n[0]))
if n[1] == '?':
  if answer[0] <= 1:
    answer.append(9)
  else:
    answer.append(3)
else:
  answer.append(int(n[1]))
if n[3] == '?':
  answer.append(5)
else:
  answer.append(int(n[3]))
if n[4] == '?':
  answer.append(9)
else:
  answer.append(int(n[4]))

print(answer)

for i in range(4):
  print(answer[i], end='')
  if i==1:
    print(':', end='')