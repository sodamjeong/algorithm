def solution(s):
    lst = list(map(int,s.split()))
    a,b = min(lst),max(lst)
    answer = f"{a} {b}"
    return answer