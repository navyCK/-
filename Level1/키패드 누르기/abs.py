def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for number in numbers :
        if number in [1,4,7] :
            left = number
            answer += 'L'
        elif number in [3,6,9] :
            right = number
            answer += 'R'
        elif number in [2,5,8,0] :
            number = 11 if number == 0 else number
            leftDist = abs(number - left)
            rightDist = abs(number - right)
            if leftDist // 3 + leftDist % 3 < rightDist // 3 + rightDist % 3 :
                left = number
                answer += 'L'
            elif leftDist // 3 + leftDist % 3 > rightDist // 3 + rightDist % 3 :
                right = number
                answer += 'R'
            elif leftDist // 3 + leftDist % 3 == rightDist // 3 + rightDist % 3 :
                if hand == 'left' :
                    left = number
                    answer += 'L'
                else :
                    right = number
                    answer += 'R'
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
