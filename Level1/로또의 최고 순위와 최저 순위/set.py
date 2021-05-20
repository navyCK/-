def solution(lottos, win_nums):
    
    cnt = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    
    return [7-max(cnt+zero,1) ,7-max(cnt,1)]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],    [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],    [20, 9, 3, 45, 4, 35]))