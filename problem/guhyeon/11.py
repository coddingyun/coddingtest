from collections import deque

n = int(input())

k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
  col, row = map(int, input().split())
  board[col][row] = 1

l = int(input())

dx = [-1,0,1,0] # 북 동 남 서
dy = [0,1,0,-1]

rot = 1
x = 1
y = 1
board[x][y] =2

q = deque()
q.append((x,y))

answer = 0
check = False
total_sec = 0
prev = 0

for i in range(l):
  sec, dir = input().split()
  sec = int(sec)
  for j in range(sec-prev):
    x += dx[rot%4]
    y += dy[rot%4]
    if x>n or x<1 or y>n or y<1 or board[x][y] == 2: # 몸이 있거나 벽일 경우
      #print(x,y)
      answer = total_sec + j + 1
      #print(total_sec, j, answer)
      check = True
      break
    q.append((x,y))
    if board[x][y] == 0: #사과 없을 시
      a, b = q.popleft()
      board[a][b] = 0
    #if board[x][y] == 1: #사과 있을 시
    board[x][y] = 2
  if check == True:
    break
  if dir == 'L':
    rot -= 1
  elif dir == 'D':
    rot += 1
  total_sec += sec - prev
  prev = sec
  #print(total_sec)
if answer == 0:
  i=1
  while True:
    x += dx[rot%4]
    y += dy[rot%4]
    if x>n or x<1 or y>n or y<1 or board[x][y] == 2: # 몸이 있거나 벽일 경우
      answer = total_sec + i
      #print(total_sec, j, answer)
      break
    q.append((x,y))
    if board[x][y] == 0: #사과 없을 시
      a, b = q.popleft()
      board[a][b] = 0
    #if board[x][y] == 1: #사과 있을 시
    board[x][y] = 2
    i+=1
print(answer)