# 문자열 내 마음대로 정렬하기 - lambda.py
def solution(strings, n):
    return sorted(strings, key=lambda x: x[n])

print(solution(["sun","bed","car"], 1))
print(solution(["abce","abcd","cdx"], 2))
