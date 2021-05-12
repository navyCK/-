def solution(n):
    temp = n**0.5
    
    if int(temp) == temp:
        return (temp + 1) ** 2
    else:
        return -1

print(solution(121))
print(solution(3))
