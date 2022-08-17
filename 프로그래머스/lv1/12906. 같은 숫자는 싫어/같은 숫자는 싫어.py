def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer or arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer