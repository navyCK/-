def solution(left, right):
    answer = 0
    arr = []
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i%j == 0:
                arr.append(j)
        if len(arr) % 2 == 0:
            answer += i
        else:
            answer += -i
        arr = []
    return answer

print(solution(13,    17))
print(solution(24,    27))