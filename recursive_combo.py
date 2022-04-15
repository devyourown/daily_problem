def recur_combo(arr, picked):
    if picked == 3:
        print(arr, end=", ")
        return
    elif picked == 2:
        end = 9
    else :
        end = 8
    for i in range(arr[picked-1]+1, end+1):
        arr[picked] = i
        recur_combo(arr, picked+1)

for i in range(8):
    arr = [-1 for _ in range(3)]
    arr[0] = i
    recur_combo(arr, 1)

