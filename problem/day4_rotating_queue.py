#https://www.acmicpc.net/problem/1021

N, M = map(int, input().split())
q = []
for i in range(1, N+1):
    q.append(i)

pick_element = list(map(int, input().split()))
ret = 0
for element in pick_element:
    q_index = q.index(element)+1
    left_distance = abs(1 - q_index)
    right_distance = abs(N - q_index)+1
    if left_distance == 0:
        q.pop(0)
    elif left_distance < right_distance:
        for i in range(left_distance):
            temp = q.pop(0)
            q.append(temp)
        ret += left_distance
        q.pop(0)
    else :
        for i in range(right_distance):
            temp = q.pop()
            q.insert(0, temp)
        ret += right_distance
        q.pop(0)
    N -= 1
print(ret)