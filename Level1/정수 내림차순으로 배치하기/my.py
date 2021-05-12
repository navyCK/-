def solution(n):
    answer = 0
    sl = list(str(n))
    sl.sort()
    sl.reverse()
    answer = int("".join(sl))
    return answer