def solution(dartResult):
    answer = []
    first = list(dartResult)
    second = []
    for i in range(len(first)):
        if first[i] == "1" and first[i+1] == "0":
            second.append("10")
        elif first[i] == "0" and first[i-1] == "1":
            continue
        else:
            second.append(first[i])
    
    for i in range(1,len(second)):
        if second[i] == 'S':
            answer.append(int(second[i-1]))
        elif second[i] == 'D':
            answer.append(int(second[i-1])**2)
        elif second[i] == 'T':
            answer.append(int(second[i-1])**3)

        if second[i] == '*':
            if len(answer) >= 2:
                answer[-1]=answer[-1]*2
                answer[-2]=answer[-2]*2
            else:
                answer[-1]=answer[-1]*2
        elif second[i] == '#':
            answer[-1]=answer[-1]*(-1)
    return sum(answer)

print(solution("1D2S0T"))
print(solution("1D2S#10S"))