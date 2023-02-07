def check(x, y, btype, answer):
    if btype == 0: #기둥
        if y == 0 or [x-1,y,1] in answer or [x,y-1,0] in answer or [x,y,1] in answer:
            return True
    elif btype == 1:
         if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                return True     
    return False

def delete(answer):
    for i in answer:
        nx = i[0]
        ny = i[1]
        dtype = i[2]
        if check(nx, ny, dtype, answer) == False:
            return False
    return True
    '''dx = [-1,-1,0]
    dy = [0,1,1]
    dx2 = [0, 1, 1]
    dy2 = [-1, 0, -1]
    if btype == 0:
        for i in range(3):
            if x+dx[i]<0 or x+dx[i]>n or y+dy[i]<0 or y+dy[i]>n:
                continue
            if check(x+dx[i], y+dy[i], btype, answer) == False:
                return False
    else:
        for i in range(3):
            if x+dx2[i]<0 or x+dx2[i]>n or y+dy2[i]<0 or y+dy2[i]>n:
                continue
            if check(x+dx2[i], y+dy2[i], btype, answer) == False:
                return False
    return True'''
      

def solution(n, build_frame):
    answer = []
    #length = len(build_frame)
    
    for i in build_frame:
        nx= i[0]
        ny=i[1]
        btype=i[2]
        ctype=i[3]
        #print(nx, ny)
        if ctype == 1:
            if check(nx,ny,btype,answer):
                answer.append([nx, ny, btype])
        elif ctype == 0:
            answer.remove([nx, ny, btype])
            if delete(answer): 
                continue
            else:
                answer.append([nx, ny, btype])
    '''for i in range(n+1):
        for j in range(n+1):
            if board[i][j] != -1:
                answer.append([i, j, board[i][j]])'''
    answer.sort()    
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))