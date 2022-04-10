N = int(input())

arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
is_printed = [0] * 1001

for i in range(N):
    ret = sorted_arr.index(arr[i])
    if is_printed[arr[i]] != 0:
        ret = ret + is_printed[arr[i]]
    print(ret, end=" ")
    is_printed[arr[i]] += 1