#n은 원형에서의 칸수
#k는 한번 들어가면 k초씩 늘어남
#infos : 들어가는 초, 입구(0)출구(1)
#example : n = 4 k = 3 [[3, 0], [5, 1], [11, 0]]
#expect: [5, 7, -1]

def solution(n, k, infos):
    answer = [-1]*len(infos)
    INF = int(1e9)
    door = [[INF]*2 for _ in range(len(infos))]
    total_time = 0
    cur_time = 0
    t = 0
    init_len = len(infos)
    while True:
        #print(len(infos), total_time)
        if total_time == 0 and init_len != len(infos):
            break
        if total_time > 0:
            print(door)
            for i in range(len(door)): # 이거 고침.
                door[i][0] -= 1
                if door[i][0] == 0 and door[i][1] == 1:
                    answer[i] = cur_time
                    door[i][0] =INF
                    #answer.append(cur_time)
                elif door[i][0] == -n//2 and door[i][1] == 0:
                    answer[i] = cur_time
                    door[i][0] =INF
            total_time -= 1
        if len(infos) > 0:
            if cur_time == infos[0][0]:
                if infos[0][1] == 0: # 0 입구 1 출구
                    door[t][0] = 0
                    door[t][1] = 0
                else:
                    door[t][0] = n//2
                    door[t][1] = 1
                total_time += k
                t += 1
                del(infos[0])
                #print(infos)

        cur_time += 1
    return answer

n1 = 4
k1 = 3
infos1 = [[3, 0], [5, 1], [100, 0]]
print(solution(n1, k1, infos1))