def solution(s):
    cnt,zero_cnt = 0,0
    while s !='1':
        zero_cnt += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
        cnt += 1
    return [cnt, zero_cnt]