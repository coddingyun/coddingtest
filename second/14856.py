n = int(input())

info = []
mnum = 0

for i in range(n):
  a, b = map(int, input().split())
  info.append([a, b])
  mnum = max(mnum, a)

domino_right = [[] for _ in range(mnum+1)]
domino_left = [[] for _ in range(mnum+1)]
info.sort()

for i in range(n):
  for j in range(n):
    if info[i][0]+1<= info[j][0] <=info[i][0]+info[i][1]:
      domino_right[info[i][0]].append(info[j][0])
    if info[i][0]-info[i][1]<= info[j][0] <=info[i][0]-1: # 자신빼고 넘어뜨릴 수 있는 도미노
      domino_left[info[i][0]].append(info[j][0])

print(domino_right)
print(domino_left)

answer = []

def btr(domino):
  if len(domino_left[domino]) != 0:
    for i in range(len(domino_left[domino])):
      answer.append(domino_left[domino][i])
      btr(domino_left[domino][i])
    domino_left[domino] = []
  
      

  