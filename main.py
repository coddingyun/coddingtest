n = int(input())

data = input().split()
print(data)

x=1
y=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

move_set=['L','R','U','D']

for word in data:
  for i in range(len(move_set)):
    if move_set[i]==word:
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<1 or nx>n or ny<1 or ny>n:
        continue
      else:
        x=nx
        y=ny

print(x, y)
    
      