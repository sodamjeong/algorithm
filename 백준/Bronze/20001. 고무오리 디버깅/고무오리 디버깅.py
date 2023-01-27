from collections import deque

start = input()
question = deque()

while 1:
    n = input()
    if n == '문제':
        question.append(n)
    elif n == '고무오리 디버깅 끝':
        if len(question) > 0:
            print('힝구')
            break
        else:
            print('고무오리야 사랑해')
            break
    else:
        if len(question) == 0:
            question.append(n)
            question.append(n)
        else:
            question.popleft()