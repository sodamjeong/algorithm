def solution(sequence, k):
    prefix = [0]
    cnt = 0
    n = 0
    m = n + 1
    answer = [0, len(sequence)]
    for i in range(len(sequence)):
        cnt += sequence[i]
        prefix.append(cnt)
    while n < m and m < len(prefix):
        if prefix[m] - prefix[n] == k:
            if (m-1) - n < (answer[1] - answer[0]):
                answer = [n, m-1]
            m += 1
        elif prefix[m] - prefix[n] < k:
            m += 1
        else:
            n += 1
    return answer