# 문자열 다루기 기본 - my(except).py

def solution(s):
    try:
        if len(s) == 4 or len(s) == 6:
            type(int(s))
            return True
        else:
            return False
        
    except ValueError:
        return False

print(solution("a234"))
print(solution("1234"))
