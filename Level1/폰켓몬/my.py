def solution(nums):
    answer = 0
    length = len(nums) // 2
    temp = list(set(nums))
    
    for value in temp :
        if(answer < length):
            answer +=1
            
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,3,2,2,2,2,2,1,4,1]))
