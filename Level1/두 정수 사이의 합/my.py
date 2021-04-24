# 두 정수 사이의 합 - my.py
def solution(a, b):
    answer = 0
    array = [a, b]
    array.sort()
    if a == b:
        answer = a
    else:
        for array[0] in range(array[0], array[1] + 1):
            answer += array[0]
    return answer
    
print(solution(3,5))
print(solution(3,3))
print(solution(5,3))
