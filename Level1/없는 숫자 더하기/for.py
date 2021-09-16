def solution(numbers):
    answer = 0
    n = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers:
        if i in n:
            answer += i
            
    return 45 - answer
    
print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))