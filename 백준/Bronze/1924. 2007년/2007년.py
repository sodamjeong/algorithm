A=["MON","TUE","WED","THU","FRI",'SAT',"SUN"]
B=[0,31,59,90,120,151,181,212,243,273,304,334]
a,b=map(int,input().split())
tmp=B[a-1]+b
print(A[tmp%7-1])
