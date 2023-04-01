import sys
input = sys.stdin.readline
number = list(map(str, input().split('-')))

answer = sum(list(map(int,number[0].split('+'))))
for i in range(1, len(number)):
    answer = answer - sum(list(map(int,number[i].split('+'))))
print(answer)
