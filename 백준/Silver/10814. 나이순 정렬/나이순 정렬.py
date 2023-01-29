import sys
input=sys.stdin.readline

judge = []

for i in range(int(input())):
    a, n = input().split()
    judge.append((i,int(a),n))
judge.sort(key=lambda x:(x[1],x[0]))

for i in judge:
    print(*(i[1],i[2]))