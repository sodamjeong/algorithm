def solution(brown, yellow):
    cnt = 1
    while 1:
        if brown/2 == ((yellow/cnt)+2)+cnt:
            answer = [(yellow/cnt)+2, cnt+2]
            break
        cnt += 1
    return answer