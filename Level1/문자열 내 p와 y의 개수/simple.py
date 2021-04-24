# 문자열 내 p와 y의 개수 - simple.py
def solution(s):
    return s.upper().count("P") == s.upper().count("Y")
        
print(solution("pPoooyY"))
print(solution("Pyy"))
