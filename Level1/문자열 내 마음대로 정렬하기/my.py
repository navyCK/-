# 문자열 내 마음대로 정렬하기 - my.py
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    
    return answer
    
print(solution(["sun","bed","car"], 1))
print(solution(["abce","abcd","cdx"], 2))
