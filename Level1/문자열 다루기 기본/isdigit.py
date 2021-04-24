# 문자열 다루기 기본 - isdigit.py

def solution(s):
    return s.isdigit() and len(s) in (4, 6)
    
print(solution("a234"))
print(solution("1234"))
