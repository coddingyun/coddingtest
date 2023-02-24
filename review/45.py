for _ in range(int(input())):
  n = int(input())
  array = list(map(int, input().split()))
  m = int(input())
  infos = []
  for _ in range(m):
    infos.append(list(map(int, input().split())))
  indegree = [0]