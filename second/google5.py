n = int(input())

rooms = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]



free = [[True]*26 for _ in range(10)]
answers = [[0]*26 for _ in range(10)]
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = list(alphabets)

for data in rooms:
  if data[0] == '+':
    floor = int(data[1])
    for i in range(len(alphabets)):
      if data[2] == alphabets[i]:
        if free[floor][i] == True:
          answers[floor][i] += 1
          free[floor][i] == False
  else:
    floor = int(data[1])
    for i in range(len(alphabets)):
      if data[2] == alphabets[i]:
        free[floor][i] == True

maxim = 0
ans_floor = 0
ans_room = 0
for i in range(10):
  for j in range(26):
    if maxim < answers[i][j]:
      maxim = answers[i][j]
      ans_floor = i
      ans_room = j

print(ans_floor, end="")
print(alphabets[ans_room])

      