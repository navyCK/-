# 오류

n = int(input())
temp = 1

for i in range(1,n):
    if temp <= n:
        temp += i*6
    else:
        print(i)
        break