def solution(N, stages):
    dic = {}
    stage = len(stages)
    for i in range(1, N+1):
        if stage != 0:
            dic[i] = stages.count(i) / stage
            stage -= stages.count(i)
        else:
            dic[i] = 0
    return sorted(dic, key = lambda x: dic[x], reverse = True)
    
print(solution(5,    [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,    [4,4,4,4,4]))