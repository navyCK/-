# 문자열 내림차순으로 배치하기 - simple.py

def solution(s):
    return ''.join(sorted(s, reverse = True))
print(solution("Zbcdefg"))