def solution(n):
    three = ''
    
    while n > 2:
        n, m = divmod(n, 3)
        three += str(m)
    three += str(n)
    
    return int(three, 3)

print(solution(45))
print(solution(125))
