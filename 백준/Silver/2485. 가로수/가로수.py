def gcd_func(a,b):
    while b!=0:
        a,b = b, a%b
    return a
n= int(input())
List=[]
a=0
b=0
for i in range(n):
    x = int(input())
    if(a==0):
        a=x
    else:
        b=x
        List.append(b-a)
        a=b
List_set = list(set(List))
gcd=List_set[0]
for i in range(1,len(List_set)):
    gcd = gcd_func(gcd,List_set[i])
cnt=0
for k in List:
    cnt += k//gcd -1
print(cnt)