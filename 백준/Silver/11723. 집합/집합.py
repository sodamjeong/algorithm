import sys

m = int(input())
rst=set()
li=[]

for i in range(m):
    li= sys.stdin.readline().split()

    if len(li) == 2: 
       li[1] =int(li[1])

    if li[0] == "add":
            rst.add(li[1])

    elif li[0] == "remove":
        if li[1] in rst:
            rst.remove(li[1])

    elif li[0] == "check":
        if li[1] in rst:
            print("1")
        else:
            print("0")

    elif li[0] == "all":
        rst = set(range(1,21))

    elif li[0] == "toggle":
        if li[1] in rst:
            rst.remove(li[1])
        else:
            rst.add(li[1])

    elif li[0] == "empty":
            rst.clear()