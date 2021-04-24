# 문자열 내 마음대로 정렬하기 - sortkey.py
def solution(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key = sortkey)
    return strings
    
print(solution(["sun","bed","car"], 1))
print(solution(["abce","abcd","cdx"], 2))
