def solution(priorities, location):
    answer = 0
        
    order = []
    cnt = 0
    l = len(priorities)
    
    while 1:
        while priorities[cnt] != max(priorities):
            cnt = (cnt + 1) % l
            
        priorities[cnt] = 0
        order.append(cnt)
        
        if len(order) == l:
            break
    
    answer = order.index(location) + 1
        
    return answer