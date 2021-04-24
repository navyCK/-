# 문자열 내 p와 y의 개수 - my.py
def solution(s):
    if s.upper().count("P") == s.upper().count("Y"):
        return True
    else:
        return False
    
print(solution("pPoooyY"))
print(solution("Pyy"))
