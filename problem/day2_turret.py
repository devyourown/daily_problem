# https://www.acmicpc.net/problem/1002
# should know equation of circle

test_case = int(input())

for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    x_distance = x2-x1
    y_distance = y2-y1
    distance = x_distance**2+y_distance**2
    possibleD1 = (r1-r2)**2
    possibleD2 = (r1+r2)**2
    if distance == 0 and possibleD1 == 0:
        print(-1)
    elif distance == possibleD1 or distance == possibleD2:
        print(1)
    elif possibleD1 < distance < possibleD2:
        print(2)
    else :
        print(0)




