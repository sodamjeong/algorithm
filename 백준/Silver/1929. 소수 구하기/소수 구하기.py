n, m = map(int, input().split())
lst = list(range(m + 1))
for i in lst[2:]:
    if lst[i] >= n:
        print(i)
    lst[i::i] = m//i * [0]