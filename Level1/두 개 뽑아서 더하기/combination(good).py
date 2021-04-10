from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))