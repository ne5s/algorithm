def solution(sizes):
    answer = 0
    w = []
    h = []
    total_max = 0
    for i in sizes:
        w.append(i[0])
        h.append(i[1])
        if i[0] > i[1]:
            if i[0] > total_max:
                total_max = i[0]
        else:
            if i[1] > total_max:
                total_max = i[1]
    w_max = max(w)
    h_max = max(h)
    if total_max == w_max:
        for i in range(len(h)):
            h_max_index = h.index(h_max)
            if w[h_max_index] < h[h_max_index]:
                temp = w[h_max_index]
                w[h_max_index] = h[h_max_index]
                h[h_max_index] = temp
            h_max = max(h)
    elif total_max == h_max:
        for i in range(len(w)):
            w_max_index = w.index(w_max)
            if w[w_max_index] > h[w_max_index]:
                temp = w[w_max_index]
                w[w_max_index] = h[w_max_index]
                h[w_max_index] = temp
            w_max = max(w)
    answer = w_max * h_max
    return answer