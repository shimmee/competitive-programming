# ARC120A
# URL:
# Date: 2021/05/23

# ---------- Ideas ----------
# dp[y][x]: マス(0, 0)からスタートして(y, x)へ行くときの通り

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
mod = 998244353
h, w = map(int, input().split())
S = [input() for _ in range(h)]
dic = {'R': 0, 'B': 1, '.': 2}

color = [[[0]*3 for _ in range(w)] for _ in range(h)]
color[0][0][dic[S[0][0]]] = 1

for y in range(h):
    for x in range(w):
        if y == x == 0: continue
        c = dic[S[y][x]]
        for i in range(3):
            color[y][x][i] = max(color[max(y-1, 0)][x][i], color[y][max(x-1, 0)][i])
        color[y][x][c] += 1

dp = [[-1 for _ in range(w)] for _ in range(h)]
dp[0][0] = 1

for y in range(h):
    for x in range(w):
        if y == x == 0: continue
        if y >= 1 and x >= 1:
            if color[y-1][x][0] != color[y][x-1][0]:
                dp[y][x] = 0
            else:
                if S[y][x] == '.':
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1])*2
                else:
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1])
        elif y >= 1:
            if S[y][x] == '.':
                dp[y][x] = dp[y - 1][x]* 2
            else:
                dp[y][x] = dp[y - 1][x]
        else:
            if S[y][x] == '.':
                dp[y][x] = dp[y][x - 1]* 2
            else:
                dp[y][x] = dp[y][x - 1]
print(dp[h-1][w-1]%mod)


# WAでした
mod = 998244353
from collections import deque, Counter
h, w = map(int, input().split())
S = [input() for _ in range(h)]
dp = [[-1 for _ in range(w)] for _ in range(h)]

diag = [[] for _ in range(h+w-1)]
for y in range(h):
    for x in range(w):
        diag[y+x].append(S[y][x])

ans = 1
for i in range(h+w-1):
    c = Counter(diag[i])
    if c['R'] > 0 and c['B'] > 0:
        ans = 0
    elif c['R'] == 0 and c['B'] == 0 and c['.']:
        ans *= 2
print(ans % mod)
# ------------------ Sample Input -------------------
2 2
B.
.R

3 3
R.R
BBR
...

2 2
BB
BB

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
