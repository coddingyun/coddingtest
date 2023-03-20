import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

dice = [0]*6

def inside_map(x, y):
  if x>=0 and x<n and y>=0 and y<m:
    return True
  return False

list1 = []
for _ in range(n):
  list1.append(list(map(int, input().split())))

commands = list(map(int, input().split()))
tx = x
ty = y
up = 1
east = 3
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
for i in range(k):
  command = commands[i]
  if command == 1 and inside_map(tx, ty+1):
    ty = ty + 1
    dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
  elif command == 2 and inside_map(tx, ty-1):
    ty = ty -1
    dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
  elif command == 3 and inside_map(tx -1, ty):
    tx = tx - 1
    dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
  elif command == 4 and inside_map(tx + 1, ty):
    tx = tx + 1
    dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
  else:
    continue

  if list1[tx][ty] == 0:
    list1[tx][ty] = dice[5]
  else:
    dice[5] = list1[tx][ty]
    list1[tx][ty] = 0

  print(dice[0])
  
  

