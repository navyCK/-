def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr = []
        result = ""
        x = format(arr1[i], 'b')
        y = format(arr2[i], 'b')
        
        x = "0"*(n-len(x)) + x
        y = "0"*(n-len(y)) + y
        
        z = str(int(x) + int(y))
        if len(z) < n:
            z = "0"*(n-len(z)) + z
        arr = list(z)
        
        for i in arr:
            if i == "0":
                result += " "
            else:
                result += "#"
            
        answer.append(result)
        
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
