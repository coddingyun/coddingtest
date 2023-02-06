row, column = map(int, input().split())
x, y, dir = map(int, input().split())

d=[[0]*column for _ in range(row)]

array=[]

for i in range(row):
  array.append(list(map(int, input().split())))
  
dx = [0, -1,0, 1]
dy = [-1, 0, 1, 0]

def turn_left():
  global dir
  dir=(dir-1)%4

count = 1
turn_time=0

while True:
  turn_left()
  next_x = x+dx[dir]
  next_y = y+dy[dir]
  if d[next_x][next_y]==0 and array[next_x][next_y]==0:
    d[next_x][next_y]=1
    x= next_x
    y=next_y
    count+=1
    turn_time=0
    continue
  else:
    turn_time+=1
  if turn_time==4:
    nx = x-dx[dir]
    ny = y-dy[dir]
    if array[nx][ny]==0:
      break

print(count)
