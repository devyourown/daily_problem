test_case = int(input())

cache = [-1] * 41

def fibo(n):
    if n == 0:
        cache[n] = (1, 0)
        return (1, 0)
    elif n == 1:
        cache[n] = (0, 1)
        return (0, 1)

    if cache[n] != -1:
        return cache[n]

    zero, one = fibo(n-1)
    another_zero, another_one = fibo(n-2)
    ret = (zero+another_zero, one+another_one)
    cache[n] = ret
    return ret

for _ in range(test_case):
    N = int(input())
    cache = [-1] * 41
    fibo(N)
    print(cache[N][0], cache[N][1])