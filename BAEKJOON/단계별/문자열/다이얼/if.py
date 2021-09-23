dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabet = list(input())

answer = 0

for i in alphabet:
    for j in dial:
        if i in j:
            answer += dial.index(j) + 3
print(answer)