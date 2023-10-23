def dfs(result, num):
    global max_num,min_num
    if num == n:
        min_num = min(min_num, result)
        max_num = max(max_num, result)
        return 
    

    for i in range(4) :
        temp = 0
        
        if cal[i] == 0: 
            continue
        
        if i == 0: 
            temp = result + lst[num]

        if i == 1: 
            temp = result - lst[num]

        if i == 2: 
            temp = result * lst[num]

        if i == 3: 
            if result < 0: 
                temp = -(-result // lst[num])
            else: 
                temp = result // lst[num]
        
        cal[i] -= 1
        dfs(temp, num+1)
        cal[i] += 1


n = int(input())
lst = list(map(int, input().split()))
cal =  list(map(int, input().split()))
max_num = -1000000001
min_num =  1000000001

dfs(lst[0], 1)
print(max_num)
print(min_num)