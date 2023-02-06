input = input()

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]

result=0

row=int(input[1])
column=int(ord(input[0]))-int(ord('a'))+1

for i in range(8):
  if column+dx[i]<1 or column+dx[i]>8 or row+dy[i]<1 or row+dy[i]>8:
    continue
  else:
    result+=1

print(result)

steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

for step in steps:
  if row+step[0]<1 or row+step[0]>8 or column+step[1]<1 or column+step[1]:
    continue
  else:
    result+=1
    
  