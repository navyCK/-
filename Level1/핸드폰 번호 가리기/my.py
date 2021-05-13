def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[len(phone_number)-4:len(phone_number)]

print(solution("01033334444"))
print(solution("027778888"))
