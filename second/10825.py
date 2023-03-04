import sys
input = sys.stdin.readline

n = int(input())

infos = []

for _ in range(n):
  infos.append(list(input().split()))

infos.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for info in infos:
  print(info[0])