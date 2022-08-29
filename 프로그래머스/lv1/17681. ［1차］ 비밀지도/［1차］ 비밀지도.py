def solution(n, arr1, arr2):
    answer = []
    arr1_to_bin = []
    arr2_to_bin = []
    for i in range(n):
        a1 = (bin(arr1[i])[2:]).zfill(n)
        a2 = (bin(arr2[i])[2:]).zfill(n)
        arr1_to_bin.append(a1)
        arr2_to_bin.append(a2)
    for i in range(n):
        arr_to_insert = ""
        for j in range(n):
            res = int(arr1_to_bin[i][j]) or int(arr2_to_bin[i][j])
            if res == 1:
                arr_to_insert += "#"
            else:
                arr_to_insert += " "
        answer.append(arr_to_insert)
        # ["01001","10100"]
    return answer