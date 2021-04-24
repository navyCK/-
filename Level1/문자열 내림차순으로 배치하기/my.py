# 문자열 내림차순으로 배치하기 - my.py

def solution(s):
    answer = ""
    array = list(s)
    array.sort()
    array.reverse()
    answer = ''.join(array)
    return answer

print(solution("Zbcdefg"))