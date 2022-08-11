def solution(id_list, report, k):
    l = len(id_list)
    answer = [0]*l
    report = list(set(report))
    singo = []
    singo_count = [0]*l
    for i in report:
        user, singos = i.split()
        singo.append([user, singos])
        singo_count[id_list.index(singos)] += 1
    for u,s in singo:
        if singo_count[id_list.index(s)] >= k:
            answer[id_list.index(u)] += 1
    return answer