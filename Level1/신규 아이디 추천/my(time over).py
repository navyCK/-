def solution(new_id):
    answer = new_id.lower()
    characters = "~!@#$%^&*()=+[{]}:?,<>/"
    
    for x in range(len(characters)):
        answer = answer.replace(characters[x],"")
        answer = answer.replace("..", ".")
        
    if answer[0] == ".":
        answer = answer[1:]
    
    if len(answer) == 0:
        answer = "aaa"

    if len(answer) >= 15:
        answer = answer[:15]
        
    if answer[-1] == ".":
        answer = answer[:-1]    
        
    if len(answer) <= 2:
        for i in range(len(answer)):
            answer = answer + answer[-1]
            if len(answer) == 3:
                break
    
    return answer
    
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


