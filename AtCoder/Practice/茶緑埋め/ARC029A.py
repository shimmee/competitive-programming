# ARC029A - 高橋君とお肉
# URL: https://atcoder.jp/contests/arc029/tasks/arc029_1
# Date: 2021/02/18

# ---------- Ideas ----------
# bit全探索
# それぞれの肉をグリル1で焼くかグリル2で焼くか全探索して，長い方の時間でansをmin更新

# ------------------- Answer --------------------
#code:python
n = int(input())
a = [int(input()) for _ in range(n)]

import itertools
all_pattern = itertools.product([0, 1], repeat=n)
ans = 10**10
for pattern in all_pattern:
    g1 = 0
    g2 = 0
    for i in range(n):
        if pattern[i] == 0:
            g1 += a[i]
        else:
            g2 += a[i]
    ans = min(ans, max(g1, g2))
print(ans)


# ------------------ Sample Input -------------------
3
1
2
4


# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc029
# N<=4のbit全探索なんてみたことない

# ----------------- Category ------------------
#AtCoder
#bit全探索