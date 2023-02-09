from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

operand = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

minans = 1e9
maxans = -1e9

def dfs(i, now):
  global add, sub, mul, div, n, minans, maxans
  if i == n:
    minans = min(minans, now)
    maxans = max(maxans, now)
  if add > 0:
    add -= 1
    dfs(i+1, now + operand[i])
    add += 1
  if sub > 0:
    sub -= 1
    dfs(i+1, now - operand[i])
    sub += 1
  if mul > 0:
    mul -= 1
    dfs(i+1, now * operand[i])
    mul += 1
  if div > 0:
    div -= 1
    dfs(i+1, int(now / operand[i]))
    div += 1

dfs(1, operand[0])
print(maxans)
print(minans)