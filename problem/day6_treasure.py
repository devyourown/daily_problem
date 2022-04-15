N = int(input())



A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

ret = 0
for i in range(N):
    max_index = 0
    max_element = 0
    for j in range(len(B)):
        if max_element < B[j]:
            max_index = j
            max_element = B[j]
    ret += A[i] * max_element
    B.pop(max_index)

print(ret)