import copy

def rotate(key):
    n = len(key) # 행 길이
    m = len(key[0]) # 열 길이
    array = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            array[j][n-i-1] = key[i][j] 
    return array

def check(fixed_lock, key, a, b):
    n = len(key) # 행 길이
    m = len(key[0]) # 열 길이
    #new_lock = copy.deepcopy(fixed_lock) -> 이걸로 하면 답은 맞다, 하지만 25번에서 시간초과가 뜬다.
    for i in range(n):
        for j in range(m):
            fixed_lock[a+i][b+j] += key[i][j] # 전역 fixed_lock에 더해짐
    x = len(fixed_lock)//3
    for i in range(x, 2*x):
        for j in range(x, 2*x):
            if fixed_lock[i][j] != 1: # 하나씩 다른지 비교하는 경우, 자물쇠 밖의 부분에서는 예외가 생긴다
                return False        
    return True

def solution(key, lock):
    n = len(lock)
    fixed_lock = [[0]*3*n for i in range(3*n)]
    for i in range(n):
        for j in range(n):
            fixed_lock[n+i][n+j] = lock[i][j]
    rotate_num = 0
    while rotate_num<4:
        for i in range(2*n):
            for j in range(2*n):
                if check(fixed_lock, key, i, j):
                    return True
                for a in range(len(key)): #key의 리스트크기로 해야한다.
                    for b in range(len(key)):
                        fixed_lock[a+i][b+j] -= key[a][b]
        rotate_num+=1
        key = rotate(key)
        
    
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))