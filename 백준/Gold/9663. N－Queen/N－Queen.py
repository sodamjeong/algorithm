import sys
n, ans = int(sys.stdin.readline()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve_dfs(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if (not a[j] and not b[i+j] and not c[i-j+n-1]) :
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve_dfs(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve_dfs(0)
print(ans)