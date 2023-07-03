def solution(p):
    if len(p) == 0:
        return ''
    n = list(p)
    cnt = 0
    for i in range(len(n)):
        if n[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            v = solution(n[i+1:])
            u = n[:i+1]
            if u[0] != '(' or u[-1] != ')':
                for j in range(1,len(u)-1):
                    if u[j] == ')':
                        u[j] = '('
                    else:
                        u[j] = ')'
                return '(' + "".join(v) + ')' + "".join(u[1:-1])
            return "".join(u) + "".join(v)