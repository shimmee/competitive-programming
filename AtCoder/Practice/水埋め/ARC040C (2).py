# ARC040C - Z塗り
# URL: https://atcoder.jp/contests/arc040/tasks/arc040_c
# Date: 2021/04/14

# ---------- Ideas ----------
# 右上を探す

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
G = []
for _ in range(n):
    G.append([i for i in input()])

ans = 0
for y in range(n):
    for x in reversed(range(n)):
        if G[y][x] == '.':
            ans += 1
            G[y] = ['o']*n
            if y < n-1:
                G[y+1][x:] = 'o'*(n-x)
print(ans)




# ------------------ Sample Input -------------------
7
...oooo
oo.....
ooooooo
ooooooo
.....oo
oooo...
ooooooo


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
