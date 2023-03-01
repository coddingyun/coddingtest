
t = int(input())

tobni = []

for _ in range(t):
  tobni.append(list(map(int, input()))) # 12시방향부터 시계방향 순서대로 0 2 4 6

#print(tobni)

r = int(input())

def rotate(str, dir):
  if dir == 1: # 시계 방향 answer[2] = str[1]
    answer = [0]*8
    for i in range(7):
      answer[i+1] = str[i]
    answer[0] = str[7]
    return answer
  else:
    answer = [0]*8
    for i in range(1,8):
      answer[i-1] = str[i]
    answer[7] = str[0]
    return answer

for _ in range(r):
  idx, dir = map(int, input().split()) # 1이 시계 방향
  idx -= 1
  lidx = []
  ldir = dir
  idx1 = idx
  while idx1-1>=0:
    if tobni[idx1][6] == tobni[idx1-1][2]:
      break
    else:
      ldir = -ldir
      lidx.append([idx1-1, ldir])
      idx1 -= 1
  ridx = []
  rdir = dir
  idx2 = idx
  while idx2+1<t:
    if tobni[idx2][2] == tobni[idx2+1][6]:
      break
    else:
      rdir = -rdir
      ridx.append([idx2+1, rdir])
      idx2 += 1
  tobni[idx] = rotate(tobni[idx], dir)
  for data in lidx:
    a, b = data
    tobni[a] = rotate(tobni[a], b)
  for data in ridx:
    a, b = data
    tobni[a] = rotate(tobni[a], b)
  #print(idx, tobni)

num = 0
for i in tobni:
  if i[0] == 1:
    num += 1

print(num)