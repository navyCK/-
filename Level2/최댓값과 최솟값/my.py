def solution(s):
    answer = ''
    s = list(map(int, s.split(' ')))
    return '{} {}'.format(min(s), max(s))
    
    
print(solution("1 2 3 4"))