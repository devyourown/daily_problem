test_case = int(input())

def pick(west, east):
    if west == N and east <= M:
        return 1

    if cache[west][east] != -1:
        return cache[west][east]

    ret = 0
    for i in range(east+1, M-(N-west)+2):
        ret += pick(west+1, i)
    cache[west][east] = ret
    return ret

for _ in range(test_case):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    else :
        cache = [[-1] * M for _ in range(N)]
        ret = 0
        for i in range(1, M-N+2):
            ret += pick(1, i)
        print(ret)
