n = int(input())

array = list(map(int, input().split()))
array.sort()

mid = int((n-1)//2)

print(array[mid])