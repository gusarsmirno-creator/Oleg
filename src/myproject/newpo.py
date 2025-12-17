def Run_Length_Encoding(arr):
    arr12 = arr[:]
    j = len(arr) - 1
    i = 0
    for _ in range(j):
        if arr[i] == arr[i + 1]:
            arr.pop(i)
            j -= 1
        else:
            i += 1
    vas = []
    vas22 = ()
    i1 = 0
    for i1 in range(len(arr)):
        f = arr12.count(arr[i1])
        vas22 = (arr[i1], f)
        vas.append(vas22)
    return vas
