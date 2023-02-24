from itertools import combinations

n, m = map(int, input().split())

alphas = list(input().split())
alphas.sort()

results = list(combinations(alphas, n))
answers = []
for i in range(len(results)):
  vowelnum = results[i].count('a') + results[i].count('e') + results[i].count('o') + results[i].count('i') + + results[i].count('u')
  nonvowelnum = n - vowelnum
  if vowelnum >= 1 and nonvowelnum >= 2:
    print(''.join(results[i]))

