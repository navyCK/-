def solution(participant, completion):
    answer = ''
    for goal in completion:
        for i in range(len(participant)):
            if participant[i] == goal:
                participant.remove(participant[i])
                break
    answer = participant[0]
    return answer
    
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
