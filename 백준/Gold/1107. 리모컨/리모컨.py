import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
btn=abs(n-100)


if m == 0:
    print(min(btn,len(str(n)))) 
    sys.exit()
else:
    lst=list(map(int,input().split()))
    
for i in range(1000001):
    i=str(i)
    
    isT=True

    for j in range(len(i)):
        if int(i[j]) in lst:
            isT=False
            break
        
    if isT==True:
        btn=min(btn, abs(n-int(i))+len(str(i)))
print(btn)   