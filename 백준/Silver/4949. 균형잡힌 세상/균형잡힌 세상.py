while 1:
    n = list(input())
    stack = []
    s = ['(',')']
    b = ['[',']']
    if len(n) == 1 and n[0] =='.':
        break
    else:
        for i in n:
            if i in ['(','['] :
                stack.append(i)
            elif i in [')',']']:
                if len(stack) == 0:
                    print('no')
                    break
                elif [stack[-1],i] == s or [stack[-1],i] == b:
                    stack.pop()
                else :
                    print('no')
                    break
        else:
            if len(stack) == 0:
                print('yes')
            else:
                print('no')
